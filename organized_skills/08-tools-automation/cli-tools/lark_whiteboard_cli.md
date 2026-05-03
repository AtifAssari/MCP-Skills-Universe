---
rating: ⭐⭐⭐
title: lark-whiteboard-cli
url: https://skills.sh/site/open.feishu.cn/lark-whiteboard-cli
---

# lark-whiteboard-cli

skills/open.feishu.cn/lark-whiteboard-cli
lark-whiteboard-cli
$ npx skills add https://open.feishu.cn
SKILL.md
  .open-platform-wrapper {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      background-color: #ffffff;
  }

  .open-platform-icon {
      width: 120px;
      height: 120px;
      display: block;
  }

  .open-platform-desc {
      margin-top: 16px;
      line-height: 22px;
      font-size: 14px;
      color: #646a73;
      text-align: center
  }

  .open-platform-back {
      border-radius: 6px;
      font-size: 14px;
      height: 32px;
      line-height: 22px;
      min-width: 80px;
      padding: 4px 11px;
      text-align: center;
      text-decoration: none;
      touch-action: manipulation;
      transition: color .1s ease-in, background-color .1s ease-in, border-color .1s ease-in, width .2s ease-in;
      user-select: none;
      white-space: nowrap;
      background: #1456f0;
      border: 1px solid #1456f0;
      color: #ffffff;
      margin-top: 16px;
  }


function parseQueryString(queryString) { // 移除开头的 "?" if (queryString.charAt(0) === '?') { queryString = queryString.substring(1); }

var params = {};
if (!queryString) return params;

// 分割参数对
var paramPairs = queryString.split('&');

for (var i = 0; i < paramPairs.length; i++) {
  var paramPair = paramPairs[i].split('=');
  var key = decodeURIComponent(paramPair[0]);
  var value = paramPair.length > 1 ? decodeURIComponent(paramPair[1]) : '';

  // 处理重复参数（转为数组）
  if (params[key] === undefined) {
    params[key] = value;
  } else if (!Array.isArray(params[key])) {
    params[key] = [params[key], value];
  } else {
    params[key].push(value);
  }
}

return params;


}

function getLocale() { var zhLang = 'zh-CN'; var enLang = 'en-US';

var queryLang = parseQueryString(window.location.search).lang;
var cookieLang = getCookieLocale();
var lang = enLang;

<!--从cookie中取值-->
function getCookieLocale() {
  var locale = '';
  var cookies = document.cookie.split('; ');
  var loclaeKey = 'open_locale';

  for (var i = 0; i < cookies.length; i++) {
    var cookie = cookies[i].trim();
    var cookieArr = cookie.split('=');
    if (cookieArr[0] === loclaeKey) {
      locale = cookieArr[1];
      break;
    }
  }
  return locale;
}

function setLocaleCookie(lang) {
  var date = new Date();
  // 300天到期
  date.setTime(date.getTime() + (300 * 24 * 60 * 60 * 1000));
  var expires = 'expires=' + date.toUTCString();
  document.cookie = 'open_locale=' + lang + '; ' + expires + '; path=/;';
}

// 获取浏览器默认语言
if (navigator.language.indexOf('en') !== -1) {
  lang = enLang;
} else if (navigator.language.indexOf('zh') !== -1) {
  lang = zhLang;
}
if (cookieLang === enLang) {
  lang = enLang;
} else if (cookieLang === zhLang) {
  lang = zhLang;
}
if (queryLang === enLang) {
  lang = enLang;
} else if (queryLang === zhLang) {
  lang = zhLang;
}
// 设置cookie
setLocaleCookie(lang);
return lang;


}

// 根据域名获取当前brand function isLarkDomain() { var defaultBrandMap = { lark: ['larksuite'], feishu: ['feishu', 'larkoffice', 'larkenterprise'], }; const { hostname } = window.location;

if (defaultBrandMap.feishu.some((item) => hostname.includes(item))) {
  return false;
}

if (defaultBrandMap.lark.some((item) => hostname.includes(item))) {
  return true;
}

if (window.domainBrand) {
  return window.domainBrand === 'lark';
}

return false;


}

var isLarkBrand = isLarkDomain();

var config = { 'zh-CN': { 'desc': '抱歉，您访问的页面不存在', 'back': '返回首页', 'title': (isLarkBrand ? 'Lark' : '飞书') + '开放平台', }, 'en-US': { 'desc': 'The page does not exist.', 'back': 'Go to homepage', 'title': (isLarkBrand ? 'Lark': 'Feishu') + ' Open Platform', }, }; var locale = getLocale(); var descObj = document.querySelector('.open-platform-desc'); var backObj = document.querySelector('.open-platform-back'); descObj.innerHTML = config[locale].desc; backObj.innerHTML = config[locale].back; document.title = config[locale].title;

Weekly Installs
2.1K
Source
open.feishu.cn
First Seen
1 day ago