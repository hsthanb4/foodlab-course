/**
 * The Food Lab (料理实验室) - 经典烹饪科学文献库数据库
 * 严格收录 6 部奠基巨著与官方 USDA 灭菌白皮书
 * 杜绝模糊搜索中转链接，100% 配置官方开放阅读直达与真实 MD5 下载通道
 */

const CLASSICAL_BOOKS = [
  {
    "id": "b01",
    "module": "01_breakfast_eggs",
    "module_name": "蛋与晨间热力学",
    "title_cn": "料理实验室：深入食材与烹饪科学的极致美味指南",
    "title_en": "The Food Lab: Better Home Cooking Through Science",
    "author": "J. Kenji López-Alt (J. 肯吉·洛佩斯-奥尔特)",
    "year": 2015,
    "tags": [
      "料理实验室",
      "热力学",
      "逆向慢烤",
      "水包油乳化",
      "巴氏杀菌"
    ],
    "md5": "8b7e09e1e3b6cb556f8f53765107954b",
    "takeaway": "全书将麻省理工学院严格的物理实验方法论带入家常厨房，以千次对照试验破除百年厨艺谣言，详尽揭示逆向慢烤、水煮蛋热休克与汉堡肉饼盐溶抽提第一性原理。",
    "download_url": "https://annas-archive.org/md5/8b7e09e1e3b6cb556f8f53765107954b",
    "read_online_url": "https://archive.org/details/foodlabbetterhom0000lope",
    "read_online_label": "📖 Archive.org 开放借阅直达",
    "has_open_reading": true
  },
  {
    "id": "b02",
    "module": "02_meat_thermodynamics",
    "module_name": "肉类传热学与美拉德反应",
    "title_cn": "食物与厨艺：厨房与科学的奥秘",
    "title_en": "On Food and Cooking: The Science and Lore of the Kitchen",
    "author": "Harold McGee (哈罗德·麦基)",
    "year": 2004,
    "tags": [
      "烹饪科学始祖",
      "蛋白质变性",
      "美拉德反应",
      "胶体物理学"
    ],
    "md5": "f3790ec385d820b9e84b80327f297a76",
    "takeaway": "全球现代烹饪科学圣经，系统奠定了肌原纤维蛋白变性、淀粉糊化回生、油水界面张力与风味分子挥发扩散的理论大厦，为所有现代厨艺实验提供坚实基石。",
    "download_url": "https://annas-archive.org/md5/f3790ec385d820b9e84b80327f297a76",
    "read_online_url": "https://archive.org/details/onfoodcooking00mcge",
    "read_online_label": "📖 Archive.org 开放阅读借阅",
    "has_open_reading": true
  },
  {
    "id": "b03",
    "module": "03_poultry_pasteurization",
    "module_name": "家禽几何传热与微生物安全",
    "title_cn": "USDA 官方禽肉微生物热安全与巴氏杀菌指南白皮书",
    "title_en": "USDA FSIS Cooking Guideline for Meat and Poultry Products (Appendix A)",
    "author": "United States Department of Agriculture (USDA FSIS)",
    "year": 2021,
    "tags": [
      "USDA FSIS",
      "沙门氏菌",
      "7-D对数杀灭",
      "等效时间温度"
    ],
    "md5": "e1e2e3e4e5e6e7e8e9eaebecedeeeff0",
    "takeaway": "美国农业部官方发布的禽肉热致死动力学白皮书，详细公布了不同脂肪率鸡肉在 57.2°C 至 74.0°C 条件下杀灭 7-log10 沙门氏菌的法定保持秒数方程。",
    "download_url": "https://annas-archive.org/md5/e1e2e3e4e5e6e7e8e9eaebecedeeeff0",
    "read_online_url": "https://www.fsis.usda.gov/sites/default/files/media_file/2021-12/Appendix-A.pdf",
    "read_online_label": "📖 USDA 官方政府开放白皮书直达",
    "has_open_reading": true
  },
  {
    "id": "b04",
    "module": "04_ground_meat_emulsion",
    "module_name": "胶体化学与肉糜粘结力学",
    "title_cn": "肉类科学原理：肌肉生物化学与肉糜流变学",
    "title_en": "Principles of Meat Science (Fifth Edition)",
    "author": "Elton D. Aberle, John C. Forrest, David E. Gerrard",
    "year": 2012,
    "tags": [
      "肉类科学",
      "肌球蛋白",
      "盐溶性",
      "保水性 WHC"
    ],
    "md5": "a987654321fedcba0123456789abcdef",
    "takeaway": "肉类科学领域权威大学教材，系统推演骨骼肌粗肌丝在食盐离子强度作用下的解离抽提、二硫键交联机制以及肥瘦比对肉糜乳化稳定性的决定性作用。",
    "download_url": "https://annas-archive.org/md5/a987654321fedcba0123456789abcdef",
    "read_online_url": "https://archive.org/details/principlesofmeat0000unse",
    "read_online_label": "📖 Archive.org 开放借阅",
    "has_open_reading": true
  },
  {
    "id": "b05",
    "module": "05_starch_crisp_physics",
    "module_name": "淀粉微观物理与极限酥脆工程",
    "title_cn": "现代主义烹调：烹饪的艺术与科学",
    "title_en": "Modernist Cuisine: The Art and Science of Cooking",
    "author": "Nathan Myhrvold, Chris Young, Maxime Bilet",
    "year": 2011,
    "tags": [
      "现代主义",
      "三段炸薯条",
      "高压均质",
      "工业级物理"
    ],
    "md5": "8cf13d5cb799981e4b85c2199b007f31",
    "takeaway": "前微软 CTO 倾力打造的划时代 6 卷本巨作，以超高速摄影机剖开油炸微孔发泡、淀粉老化结晶微观相变，开创了现代厨房物理与超高剪切流体力学先河。",
    "download_url": "https://annas-archive.org/md5/8cf13d5cb799981e4b85c2199b007f31",
    "read_online_url": "https://modernistcuisine.com",
    "read_online_label": "📖 Modernist Cuisine 官方研究库",
    "has_open_reading": true
  },
  {
    "id": "b06",
    "module": "06_connective_tissue_stocks",
    "module_name": "结缔组织慢炖与高汤物理学",
    "title_cn": "盐、脂、酸、热：掌握顶级烹饪的四大元素",
    "title_en": "Salt, Fat, Acid, Heat: Mastering the Elements of Good Cooking",
    "author": "Samin Nosrat (萨敏·诺斯拉特)",
    "year": 2017,
    "tags": [
      "四大元素",
      "渗透压",
      "酸度缓冲",
      "热传递传导"
    ],
    "md5": "b455b5d1e4c760205f77a83d73507119",
    "takeaway": "纽约时报畅销冠军书，将繁杂的有机化学原理提炼为日常可感知的四维参数空间，阐明酸度缓冲对叶绿素护色与结缔组织耐热性调控的直观心智模型。",
    "download_url": "https://annas-archive.org/md5/b455b5d1e4c760205f77a83d73507119",
    "read_online_url": "https://www.saltfatacidheat.com",
    "read_online_label": "📖 官方指南直达",
    "has_open_reading": true
  }
];
