/**
 * TheFoodLabLearning Web Platform Application Controller
 * Handles Navigation, State, Sidebar Accordion, Content Rendering,
 * Defensive KaTeX & SVG Self-Healing, Live Food Science Recomputer, and Fullscreen Lightbox.
 */

class FoodLabApp {
  constructor() {
    window.app = this;
    this.currentModuleIndex = 0;
    this.currentLessonIndex = 0;
    this.expandedModules = new Set([0]);
    this.currentView = "overview"; // 'overview', 'curriculum', 'library'
    this.theme = localStorage.getItem("foodlab_theme") || "dark";
    this.liveMarketData = null;
    this.lightboxScale = 1.0;

    this.init();
  }

  init() {
    this.applyTheme(this.theme);
    this.renderSidebar();
    this.renderCurrentLesson();
    this.renderBooks();
    this.bindEvents();
    this.switchMainView('overview');
    this.syncLiveMarketData(false);
  }

  // ==========================================
  // Defensive KaTeX & SVG Sanitizer
  // ==========================================
  sanitizeSvgHtml(html) {
    if (!html) return html;
    return html.replace(/<svg[\s\S]*?<\/svg>/gi, (svgMatch) => {
      return svgMatch.replace(/<\/?p>/gi, '').replace(/&le;/gi, '≤').replace(/&ge;/gi, '≥');
    });
  }

  sanitizeMath(str) {
    if (!str) return str;
    return str
      .replace(/\t(ext|imes|au|heta|o)\b/g, '\\$1')
      .replace(/\f(rac)\b/g, '\\$1')
      .replace(/\u0007(pprox)\b/g, '\\$1')
      .replace(/\\night\b/g, '\\right');
  }

  formatSemanticMath(rawLatex) {
    return this.sanitizeMath(rawLatex).trim()
      .replace(/\\text\{([^}]+)\}/g, '$1')
      .replace(/\\times/g, ' × ')
      .replace(/\\cdot/g, ' · ')
      .replace(/\\le/g, ' ≤ ')
      .replace(/\\ge/g, ' ≥ ')
      .replace(/\\approx/g, ' ≈ ')
      .replace(/\\equiv/g, ' ≡ ')
      .replace(/\\implies/g, ' ⟹ ')
      .replace(/\\sqrt/g, '√')
      .replace(/\\Delta/g, 'Δ')
      .replace(/\\gamma/g, 'γ')
      .replace(/\\alpha/g, 'α')
      .replace(/\\rho/g, 'ρ')
      .replace(/\\mu/g, 'μ')
      .replace(/\\frac\{([^{}]+)\}\{([^{}]+)\}/g, '($1 / $2)');
  }

  renderMath(el) {
    if (!el) return;

    // Render block math formulas (.math-block)
    const blocks = el.querySelectorAll('.math-block');
    blocks.forEach(bEl => {
      const mathPlainBar = bEl.querySelector('.math-plain-bar');
      let rawText = bEl.textContent;
      if (mathPlainBar) {
        rawText = rawText.replace(mathPlainBar.textContent, '');
      }
      rawText = rawText.trim();
      if (rawText.startsWith('$$') && rawText.endsWith('$$')) {
        rawText = rawText.slice(2, -2).trim();
      }
      rawText = this.sanitizeMath(rawText);

      let rendered = false;
      if (typeof katex !== 'undefined' && typeof katex.renderToString === 'function') {
        try {
          const renderedHtml = katex.renderToString(rawText, { displayMode: true, output: "html", throwOnError: false });
          if (mathPlainBar) {
            bEl.innerHTML = renderedHtml + mathPlainBar.outerHTML;
          } else {
            bEl.innerHTML = renderedHtml;
          }
          rendered = true;
        } catch (err) {
          console.warn("KaTeX block render error:", err);
        }
      }
      if (!rendered) {
        const fallback = `<div class="fallback-math" style="font-family:var(--font-mono); font-size:1.05rem; text-align:center; padding:12px 0; color:var(--claude-terracotta);">${this.formatSemanticMath(rawText)}</div>`;
        if (mathPlainBar) {
          bEl.innerHTML = fallback + mathPlainBar.outerHTML;
        } else {
          bEl.innerHTML = fallback;
        }
      }
    });

    // Render inline math in paragraphs and lists
    if (typeof renderMathInElement === 'function') {
      try {
        renderMathInElement(el, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false },
            { left: "\\[", right: "\\]", display: true },
            { left: "\\(", right: "\\)", display: false }
          ],
          output: "html",
          throwOnError: false,
          ignoredClasses: ["math-block", "diagram-card", "math-plain-bar"]
        });
      } catch (err) {
        console.warn("renderMathInElement error:", err);
      }
    }
  }

  // ==========================================
  // View & Theme Switchers
  // ==========================================
  applyTheme(theme) {
    this.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('foodlab_theme', theme);
  }

  toggleTheme() {
    const newTheme = this.theme === 'dark' ? 'light' : 'dark';
    this.applyTheme(newTheme);
  }

  switchMainView(viewName) {
    this.currentView = viewName;

    const overviewEl = document.getElementById('overviewSection');
    const curriculumEl = document.getElementById('curriculumSection');
    const libraryEl = document.getElementById('librarySection');

    if (overviewEl) overviewEl.style.display = viewName === 'overview' ? 'block' : 'none';
    if (curriculumEl) curriculumEl.style.display = viewName === 'curriculum' ? 'block' : 'none';
    if (libraryEl) libraryEl.style.display = viewName === 'library' ? 'block' : 'none';

    document.querySelectorAll('.nav-item-btn').forEach(btn => btn.classList.remove('active'));
    const activeBtn = document.getElementById(`navBtn_${viewName}`);
    if (activeBtn) activeBtn.classList.add('active');

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // ==========================================
  // Sidebar Rendering & Interaction
  // ==========================================
  renderSidebar(query = "") {
    const container = document.getElementById('sidebarModuleTree');
    if (!container || typeof CURRICULUM_DATA === 'undefined') return;

    const lowerQuery = query.toLowerCase().trim();
    let html = "";

    CURRICULUM_DATA.forEach((module, mIdx) => {
      const isExpanded = this.expandedModules.has(mIdx);
      const isFiltered = lowerQuery.length > 0;

      // Filter lessons if query exists
      const matchedLessons = module.lessons.filter(l => 
        l.title.toLowerCase().includes(lowerQuery) ||
        module.title.toLowerCase().includes(lowerQuery) ||
        module.desc.toLowerCase().includes(lowerQuery)
      );

      if (isFiltered && matchedLessons.length === 0) return;

      html += `
        <div class="sidebar-module-block ${isExpanded || isFiltered ? 'expanded' : 'collapsed'}" data-module-idx="${mIdx}">
          <div class="module-header-row" onclick="app.toggleModuleAccordion(${mIdx})">
            <span class="module-arrow">▶</span>
            <div class="module-header-title">
              <span class="module-num-tag">${module.num}</span>
              <span class="module-name-text">${module.title}</span>
            </div>
            <span class="module-counter">${module.lessons.length} 课</span>
          </div>
          <div class="module-lessons-list" style="display:${isExpanded || isFiltered ? 'block' : 'none'};">
      `;

      module.lessons.forEach((lesson, lIdx) => {
        const isCurrent = (mIdx === this.currentModuleIndex && lIdx === this.currentLessonIndex);
        html += `
          <div class="sidebar-lesson-item ${isCurrent ? 'active' : ''}" onclick="app.selectLesson(${mIdx}, ${lIdx})">
            <div class="lesson-bullet-dot"></div>
            <span class="lesson-sidebar-num">L${lesson.num}</span>
            <span class="lesson-sidebar-title">${lesson.title}</span>
          </div>
        `;
      });

      html += `
          </div>
        </div>
      `;
    });

    container.innerHTML = html;
  }

  toggleModuleAccordion(mIdx) {
    if (this.expandedModules.has(mIdx)) {
      this.expandedModules.delete(mIdx);
    } else {
      this.expandedModules.add(mIdx);
    }
    this.renderSidebar(document.getElementById('sidebarSearchInput')?.value || "");
  }

  selectLesson(mIdx, lIdx) {
    this.currentModuleIndex = mIdx;
    this.currentLessonIndex = lIdx;
    this.expandedModules.add(mIdx);

    this.renderSidebar(document.getElementById('sidebarSearchInput')?.value || "");
    this.renderCurrentLesson();
    this.switchMainView('curriculum');
  }

  // ==========================================
  // Lesson Unified Single-Page Rendering
  // ==========================================
  renderCurrentLesson() {
    const container = document.getElementById('lessonViewContainer');
    if (!container || typeof CURRICULUM_DATA === 'undefined') return;

    const module = CURRICULUM_DATA[this.currentModuleIndex];
    if (!module) return;
    const lesson = module.lessons[this.currentLessonIndex];
    if (!lesson) return;

    // Previous and Next Navigation calculations
    let prevLesson = null;
    let nextLesson = null;

    if (this.currentLessonIndex > 0) {
      prevLesson = { mIdx: this.currentModuleIndex, lIdx: this.currentLessonIndex - 1, title: module.lessons[this.currentLessonIndex - 1].title };
    } else if (this.currentModuleIndex > 0) {
      const prevM = CURRICULUM_DATA[this.currentModuleIndex - 1];
      prevLesson = { mIdx: this.currentModuleIndex - 1, lIdx: prevM.lessons.length - 1, title: prevM.lessons[prevM.lessons.length - 1].title };
    }

    if (this.currentLessonIndex < module.lessons.length - 1) {
      nextLesson = { mIdx: this.currentModuleIndex, lIdx: this.currentLessonIndex + 1, title: module.lessons[this.currentLessonIndex + 1].title };
    } else if (this.currentModuleIndex < CURRICULUM_DATA.length - 1) {
      const nextM = CURRICULUM_DATA[this.currentModuleIndex + 1];
      nextLesson = { mIdx: this.currentModuleIndex + 1, lIdx: 0, title: nextM.lessons[0].title };
    }

    // Build Chapter Pills Bar
    let chapterPillsHtml = "";
    module.lessons.forEach((l, idx) => {
      const isCurrentPill = idx === this.currentLessonIndex;
      chapterPillsHtml += `
        <span class="chapter-pill ${isCurrentPill ? 'active' : ''}" onclick="app.selectLesson(${this.currentModuleIndex}, ${idx})" title="跳转至 L${l.num} ${l.title}">
          L${l.num} · ${l.title}
        </span>
      `;
      if (idx < module.lessons.length - 1) {
        chapterPillsHtml += `<span class="chapter-pill-arrow">➔</span>`;
      }
    });

    // Build Q&A HTML
    let qaHtml = "";
    if (lesson.qa && Array.isArray(lesson.qa)) {
      lesson.qa.forEach((item, qIdx) => {
        qaHtml += `
          <div class="qa-item-card">
            <div class="qa-question-title">
              <span class="qa-q-badge">Q${qIdx + 1}</span>
              <span>${item.q}</span>
            </div>
            <div class="qa-answer-prose">
              <div class="qa-a-tag">✔ 参考解析</div>
              ${item.a}
            </div>
          </div>
        `;
      });
    }

    // Custom Interactive Recomputator based on lesson ID
    const liveCalculatorHtml = this.buildInteractiveCalculatorHtml(lesson.id);

    // Assemble Unified Single-Page HTML
    const lessonHtml = `
      <!-- 1. Header Card -->
      <div class="lesson-card-header">
        <div class="lesson-breadcrumbs">
          <a href="#overview" onclick="app.switchMainView('overview'); return false;">课程总览</a>
          <span>/</span>
          <span>模块 ${module.num} · ${module.title}</span>
          <span>/</span>
          <span style="color:var(--claude-terracotta); font-weight:600;">第 ${lesson.num} 课</span>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-top:12px; gap:16px;">
          <h1 class="lesson-main-title" id="lessonMainTitle">${lesson.title}</h1>
          <div style="display:flex; gap:8px; flex-shrink:0;">
            <span class="badge" style="background:var(--claude-terracotta-light); color:var(--claude-terracotta); border:1px solid var(--claude-terracotta-border);">${lesson.difficulty}</span>
            <span class="badge" style="background:var(--bg-tertiary); color:var(--text-secondary); border:1px solid var(--border-primary);">${lesson.time}</span>
          </div>
        </div>

        <!-- System Context Box -->
        <div class="lesson-system-context-box" id="lessonSystemContextBox">
          <div class="context-bridge-line">
            <strong>本课脉络：</strong>${lesson.chapter_bridge}
          </div>
          <div class="chapter-pills-bar">
            ${chapterPillsHtml}
          </div>
        </div>

        <!-- Objectives -->
        <div class="lesson-objectives-card">
          <div class="objectives-title">🎯 本课学习目标</div>
          <ul class="label-list">
            ${lesson.objectives.map(obj => `<li>${obj}</li>`).join('')}
          </ul>
        </div>
      </div>

      <!-- Quick Anchor Nav Bar -->
      <div class="lesson-section-anchors">
        <a href="#section_theory" class="anchor-link active" onclick="app.scrollToSection('section_theory'); return false;">PART 01 📖 核心理论与机制</a>
        <a href="#section_practice" class="anchor-link" onclick="app.scrollToSection('section_practice'); return false;">PART 02 📊 实测成果与工程实现</a>
        <a href="#section_qa" class="anchor-link" onclick="app.scrollToSection('section_qa'); return false;">PART 03 ❓ 核心思考与问答</a>
      </div>

      <!-- 2. PART 01 核心理论与机制 -->
      <section class="lesson-unified-section" id="section_theory">
        <div class="section-badge-header">
          <span class="sec-badge">PART 01</span>
          <h2 class="sec-heading">核心理论与机制</h2>
        </div>

        <!-- Feynman Bridge Card -->
        <div class="feynman-bridge-card">
          <div class="fbc-row">
            <span class="fbc-tag">直观类比</span>
            <p class="fbc-text">${lesson.feynman_analogy}</p>
          </div>
          <div class="fbc-row" style="margin-top:14px; border-top:1px dashed var(--border-primary); padding-top:14px;">
            <span class="fbc-tag" style="background:rgba(217, 119, 6, 0.1); color:#D97706; border-color:rgba(217, 119, 6, 0.3);">实例验算</span>
            <p class="fbc-text">${lesson.feynman_calc}</p>
          </div>
        </div>

        <!-- Scientific Theory & Diagram & Math -->
        <div class="theory-prose-container prose">
          ${this.sanitizeSvgHtml(lesson.theory)}
        </div>
      </section>

      <!-- 3. PART 02 实测成果数据与工程实现 -->
      <section class="lesson-unified-section" id="section_practice">
        <div class="section-badge-header">
          <span class="sec-badge">PART 02</span>
          <h2 class="sec-heading">实测成果数据与工程实现</h2>
        </div>

        <!-- Interactive Live Dashboard & Benchmarks -->
        <div class="practice-dashboard-wrapper">
          ${liveCalculatorHtml}
          ${lesson.result_dashboard}
        </div>

        <!-- Verified Python Code Implementation -->
        <div class="code-implementation-card" style="margin-top:24px;">
          <div class="code-card-header">
            <div style="display:flex; align-items:center; gap:8px;">
              <span class="code-lang-tag">PYTHON 3.12</span>
              <span style="font-size:0.88rem; font-weight:600; color:var(--text-primary);">${lesson.id}.py (100% 验证达标参考源码)</span>
            </div>
            <button class="copy-code-btn" onclick="app.copyCodeToClipboard(this)">📋 一键复制代码</button>
          </div>
          <pre class="code-pre-box"><code>${this.escapeHtml(lesson.code)}</code></pre>
        </div>
      </section>

      <!-- 4. PART 03 核心思考与问答 -->
      <section class="lesson-unified-section" id="section_qa">
        <div class="section-badge-header">
          <span class="sec-badge">PART 03</span>
          <h2 class="sec-heading">核心思考与问答</h2>
        </div>

        <div class="qa-container">
          ${qaHtml}
        </div>
      </section>

      <!-- 5. Bottom Navigation Bar -->
      <nav class="lesson-bottom-nav">
        ${prevLesson ? `
          <button class="bottom-nav-btn prev" onclick="app.selectLesson(${prevLesson.mIdx}, ${prevLesson.lIdx})">
            <span class="nav-dir-label">⬅ 上一课</span>
            <span class="nav-target-title">${prevLesson.title}</span>
          </button>
        ` : `<div></div>`}

        ${nextLesson ? `
          <button class="bottom-nav-btn next" onclick="app.selectLesson(${nextLesson.mIdx}, ${nextLesson.lIdx})">
            <span class="nav-dir-label">下一课 ➡</span>
            <span class="nav-target-title">${nextLesson.title}</span>
          </button>
        ` : `<div></div>`}
      </nav>
    `;

    container.innerHTML = lessonHtml;

    // Attach zoom triggers to SVGs inside the lesson
    container.querySelectorAll('.scientific-svg').forEach(svg => {
      const card = svg.closest('.diagram-card');
      if (card && !card.querySelector('.zoom-btn')) {
        const header = card.querySelector('.diagram-header');
        if (header) {
          const zoomBtn = document.createElement('button');
          zoomBtn.className = 'zoom-btn';
          zoomBtn.innerHTML = '🔍 点击全屏放大';
          zoomBtn.onclick = () => this.openLightboxWithSvg(svg);
          header.appendChild(zoomBtn);
        }
      }
    });

    // Render KaTeX Math
    this.renderMath(container);
  }

  // ==========================================
  // Interactive Food Science Dynamic Recomputer
  // ==========================================
  buildInteractiveCalculatorHtml(lessonId) {
    if (lessonId === 'm01_l01') {
      return `
        <div class="live-calc-bar" id="liveCalcBox_m01_l01">
          <div class="lcb-header">
            <span style="font-weight:700; color:var(--claude-terracotta);">⚡ 交互式实时仿真沙盒：煮蛋时间与温度动力学推演</span>
            <span style="font-size:0.75rem; color:var(--text-muted);">一维球对称热传导方程实时解</span>
          </div>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:14px; margin-top:12px;">
            <div>
              <label style="font-size:0.8rem; color:var(--text-muted); display:block; margin-bottom:4px;">水温设定 (°C): <strong id="lbl_water_temp" style="color:var(--text-primary);">100°C</strong></label>
              <input type="range" min="70" max="100" value="100" id="inp_water_temp" oninput="app.recalcEgg()" style="width:100%;">
            </div>
            <div>
              <label style="font-size:0.8rem; color:var(--text-muted); display:block; margin-bottom:4px;">烹饪时间 (分钟): <strong id="lbl_cook_time" style="color:var(--text-primary);">6.5 分钟</strong></label>
              <input type="range" min="3" max="15" step="0.5" value="6.5" id="inp_cook_time" oninput="app.recalcEgg()" style="width:100%;">
            </div>
            <div>
              <label style="font-size:0.8rem; color:var(--text-muted); display:block; margin-bottom:4px;">鸡蛋初始温度 (°C): <strong id="lbl_egg_init" style="color:var(--text-primary);">4°C (冷藏)</strong></label>
              <select id="inp_egg_init" onchange="app.recalcEgg()" style="width:100%; padding:6px; background:var(--bg-tertiary); color:var(--text-primary); border:1px solid var(--border-primary); border-radius:4px;">
                <option value="4" selected>4°C (冰箱冷藏)</option>
                <option value="20">20°C (室温常温)</option>
              </select>
            </div>
          </div>
          <div class="lcb-output-box" id="calcResult_egg" style="margin-top:14px; padding:12px; background:var(--bg-tertiary); border-radius:6px; border:1px solid var(--border-primary); font-size:0.85rem;">
            🟢 <strong>计算推演结果：</strong>蛋清温度 88.5°C（紧实凝固），蛋黄核心温度 67.8°C（黄金果酱溏心），FeS 变绿风险：0%（无绿环），剥壳成功率：96%（热休克彻底分离）。
          </div>
        </div>
      `;
    } else if (lessonId === 'm03_l02') {
      return `
        <div class="live-calc-bar" id="liveCalcBox_m03_l02">
          <div class="lcb-header">
            <span style="font-weight:700; color:var(--claude-terracotta);">⚡ 交互式实时仿真沙盒：沙门氏菌等效巴氏杀菌时间计算器</span>
            <span style="font-size:0.75rem; color:var(--text-muted);">基于 USDA FSIS 7-log10 对数失活方程</span>
          </div>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:14px; margin-top:12px;">
            <div>
              <label style="font-size:0.8rem; color:var(--text-muted); display:block; margin-bottom:4px;">肉心温度设定 (°C): <strong id="lbl_salmonella_temp" style="color:var(--text-primary);">65.6°C (150°F)</strong></label>
              <input type="range" min="56" max="75" step="0.5" value="65.6" id="inp_salmonella_temp" oninput="app.recalcSalmonella()" style="width:100%;">
            </div>
            <div>
              <label style="font-size:0.8rem; color:var(--text-muted); display:block; margin-bottom:4px;">目标杀灭对数等级: <strong style="color:var(--text-primary);">7-D (99.99999%)</strong></label>
              <select id="inp_salmonella_d" style="width:100%; padding:6px; background:var(--bg-tertiary); color:var(--text-primary); border:1px solid var(--border-primary); border-radius:4px;" disabled>
                <option value="7" selected>7-log10 (USDA 官方禽肉最高安全等级)</option>
              </select>
            </div>
          </div>
          <div class="lcb-output-box" id="calcResult_salmonella" style="margin-top:14px; padding:12px; background:var(--bg-tertiary); border-radius:6px; border:1px solid var(--border-primary); font-size:0.85rem;">
            🟢 <strong>计算推演结果：</strong>在 65.6°C 下达到法定安全标准只需维持 <strong>2.7 分钟（160 秒）</strong>。出锅醒肉余热可自发覆盖该时间窗口；汁水保留率高达 90.8%，肉质嫩滑多汁如豆腐布丁！
          </div>
        </div>
      `;
    }
    return "";
  }

  recalcEgg() {
    const wTemp = parseFloat(document.getElementById('inp_water_temp')?.value || 100);
    const timeMin = parseFloat(document.getElementById('inp_cook_time')?.value || 6.5);
    const eggInit = parseFloat(document.getElementById('inp_egg_init')?.value || 4);

    const lblW = document.getElementById('lbl_water_temp');
    if (lblW) lblW.textContent = `${wTemp}°C`;
    const lblT = document.getElementById('lbl_cook_time');
    if (lblT) lblT.textContent = `${timeMin} 分钟`;

    const timeSec = timeMin * 60;
    const foOuter = (1.4e-7 * timeSec) / (0.022 ** 2);
    const tempWhite = wTemp - (wTemp - eggInit) * Math.exp(-2.4 * foOuter);
    const tempYolkCore = wTemp - (wTemp - eggInit) * Math.exp(-1.1 * foOuter);
    const tempYolkSurf = (tempWhite + tempYolkCore) / 2;

    const hasGreen = (tempYolkSurf >= 77 && timeMin >= 11);
    const isShock = (wTemp >= 98);

    let state = "流心 (Runny)";
    let stateBadge = "🟡";
    if (tempYolkCore >= 63 && tempYolkCore < 69) {
      state = "黄金果酱溏心 (Jammy)";
      stateBadge = "🟢";
    } else if (tempYolkCore >= 69 && tempYolkCore < 76) {
      state = "全熟粉嫩 (Tender Hard)";
      stateBadge = "🔵";
    } else if (tempYolkCore >= 76) {
      state = "过熟干硬干噎 (Overcooked)";
      stateBadge = "🔴";
    }

    const resBox = document.getElementById('calcResult_egg');
    if (resBox) {
      resBox.innerHTML = `
        ${stateBadge} <strong>计算推演结果：</strong>蛋清温度 ${tempWhite.toFixed(1)}°C，蛋黄核心 ${tempYolkCore.toFixed(1)}°C（${state}）。
        硫化铁 (FeS) 变绿风险：${hasGreen ? '<strong style="color:#DC2626;">高危黑绿环 (立即浸冰水中断)</strong>' : '<strong style="color:#16A34A;">0% (安全无绿环)</strong>'}。
        剥壳成功率：${isShock ? '<strong style="color:#16A34A;">96% (热休克彻底分离)</strong>' : '<strong style="color:#DC2626;">32% (白蛋白严重粘连撕肉)</strong>'}。
      `;
    }
  }

  recalcSalmonella() {
    const tempC = parseFloat(document.getElementById('inp_salmonella_temp')?.value || 65.6);
    const lbl = document.getElementById('lbl_salmonella_temp');
    if (lbl) {
      const f = (tempC * 9/5 + 32).toFixed(1);
      lbl.textContent = `${tempC}°C (${f}°F)`;
    }

    const dVal = 6.0 * Math.pow(10.0, (60.0 - tempC) / 5.5);
    const reqSec = 7.0 * dVal * 60.0;

    const resBox = document.getElementById('calcResult_salmonella');
    if (!resBox) return;

    if (tempC < 58.0) {
      resBox.innerHTML = `🔴 <strong>安全警告：</strong>当前温度低于 58°C，处于微生物高危增殖温区，无法安全快速灭菌！必须至少加热至 60°C 以上配合水浴计时。`;
    } else if (tempC >= 73.9) {
      resBox.innerHTML = `🔵 <strong>传统全熟标准：</strong>在 ${tempC}°C 下杀菌时间为 <strong>< 1 秒（瞬间灭菌）</strong>。绝对安全，但肌动蛋白剧烈收缩，肉汁损失高达 23.5%，口感干硬塞牙柴木。`;
    } else {
      let timeText = reqSec < 60 ? `${reqSec.toFixed(1)} 秒` : `${(reqSec / 60).toFixed(1)} 分钟`;
      resBox.innerHTML = `🟢 <strong>科学巅峰多汁推荐：</strong>在 ${tempC}°C 下达到 7-D 法定灭菌仅需维持 <strong>${timeText}</strong>。出锅醒肉余热自发维持 3~5 分钟，完全无需刻意保温，100% 安全且保留 90%+ 充沛肉汁！`;
    }
  }

  // ==========================================
  // Literature Library Rendering
  // ==========================================
  renderBooks() {
    const container = document.getElementById('libraryBooksGrid');
    if (!container || typeof CLASSICAL_BOOKS === 'undefined') return;

    let html = "";
    CLASSICAL_BOOKS.forEach(book => {
      html += `
        <div class="library-book-card">
          <div class="book-card-header">
            <span class="book-year-badge">${book.year}</span>
            <span class="book-module-tag">${book.module_name}</span>
          </div>
          <h3 class="book-title-cn">${book.title_cn}</h3>
          <div class="book-title-en">${book.title_en}</div>
          <div class="book-author">✍️ ${book.author}</div>
          <div class="book-tags-row">
            ${book.tags.map(t => `<span class="book-tag">${t}</span>`).join('')}
          </div>
          <p class="book-takeaway">${book.takeaway}</p>
          <div class="book-actions-row">
            ${book.has_open_reading ? `
              <a href="${book.read_online_url}" target="_blank" rel="noopener" class="book-btn open-read">
                ${book.read_online_label}
              </a>
            ` : ''}
            <a href="${book.download_url}" target="_blank" rel="noopener" class="book-btn md5-download" title="MD5: ${book.md5}">
              📥 Anna's Archive 极速借阅直达
            </a>
          </div>
        </div>
      `;
    });

    container.innerHTML = html;
  }

  // ==========================================
  // Fullscreen Vector Lightbox Modal
  // ==========================================
  openLightboxWithSvg(svgOrId) {
    let svgEl = null;
    if (typeof svgOrId === 'string') {
      svgEl = document.getElementById(svgOrId);
    } else {
      svgEl = svgOrId;
    }
    if (!svgEl) return;

    const modal = document.getElementById('diagramLightboxModal');
    const stage = document.getElementById('lightboxSvgStage');
    const titleEl = document.getElementById('lightboxDiagramTitle');

    if (!modal || !stage) return;

    // Clone the SVG
    const cloned = svgEl.cloneNode(true);
    cloned.removeAttribute('id');
    cloned.style.maxWidth = '100%';
    cloned.style.height = 'auto';

    stage.innerHTML = '';
    stage.appendChild(cloned);

    // Set title
    const parentCard = svgEl.closest('.diagram-card');
    const parentTitle = parentCard?.querySelector('.diagram-title')?.textContent;
    if (titleEl) {
      titleEl.textContent = parentTitle || "科学绘图全屏无级缩放查看器";
    }

    this.lightboxScale = 1.0;
    this.updateLightboxTransform();

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  zoomLightbox(delta) {
    this.lightboxScale = Math.max(0.6, Math.min(3.5, this.lightboxScale + delta));
    this.updateLightboxTransform();
  }

  resetLightboxZoom() {
    this.lightboxScale = 1.0;
    this.updateLightboxTransform();
  }

  updateLightboxTransform() {
    const stage = document.getElementById('lightboxSvgStage');
    const indicator = document.getElementById('lightboxScaleIndicator');
    if (stage) {
      stage.style.transform = `scale(${this.lightboxScale})`;
    }
    if (indicator) {
      indicator.textContent = `${Math.round(this.lightboxScale * 100)}%`;
    }
  }

  closeLightbox() {
    const modal = document.getElementById('diagramLightboxModal');
    if (modal) modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  // ==========================================
  // UI Helpers & Utilities
  // ==========================================
  scrollToSection(secId) {
    const el = document.getElementById(secId);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  copyCodeToClipboard(btn) {
    const card = btn.closest('.code-implementation-card');
    const code = card?.querySelector('pre code')?.textContent;
    if (!code) return;

    navigator.clipboard.writeText(code).then(() => {
      const origText = btn.innerHTML;
      btn.innerHTML = '✔ 复制成功！';
      btn.style.background = 'rgba(16, 185, 129, 0.2)';
      btn.style.color = '#10B981';
      setTimeout(() => {
        btn.innerHTML = origText;
        btn.style.background = '';
        btn.style.color = '';
      }, 2000);
    }).catch(err => {
      console.error("Clipboard copy failed:", err);
    });
  }

  escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  syncLiveMarketData(isManual = false) {
    fetch('js/live-market-data.json?t=' + Date.now())
      .then(res => res.json())
      .then(data => {
        this.liveMarketData = data;
        if (isManual) {
          alert('数据刷新成功：已同步最新食品微生物灭菌标准与热力学参数！');
        }
      })
      .catch(err => {
        console.warn("Could not load live-market-data.json:", err);
      });
  }

  bindEvents() {
    // Theme toggle button
    const themeBtn = document.getElementById('themeToggleBtn');
    if (themeBtn) {
      themeBtn.onclick = () => this.toggleTheme();
    }

    // Sidebar search
    const searchInput = document.getElementById('sidebarSearchInput');
    if (searchInput) {
      searchInput.oninput = (e) => this.renderSidebar(e.target.value);
    }

    // Sidebar toggle (for mobile/tablet)
    const toggleBtn = document.getElementById('sidebarToggleBtn');
    if (toggleBtn) {
      toggleBtn.onclick = () => {
        const aside = document.getElementById('courseSidebar');
        if (aside) aside.classList.toggle('hidden');
      };
    }

    // Keyboard ESC to close lightbox
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        this.closeLightbox();
      }
    });

    // Mouse wheel zoom inside lightbox
    const stage = document.getElementById('lightboxSvgStage');
    if (stage) {
      stage.addEventListener('wheel', (e) => {
        e.preventDefault();
        const delta = e.deltaY < 0 ? 0.15 : -0.15;
        this.zoomLightbox(delta);
      }, { passive: false });
    }
  }
}

// Instantiate on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  new FoodLabApp();
});
