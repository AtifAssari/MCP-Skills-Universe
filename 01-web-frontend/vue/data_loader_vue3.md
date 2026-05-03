---
rating: ⭐⭐⭐
title: data-loader-vue3
url: https://skills.sh/lchrennew/data-loader-vue3/data-loader-vue3
---

# data-loader-vue3

skills/lchrennew/data-loader-vue3/data-loader-vue3
data-loader-vue3
Installation
$ npx skills add https://github.com/lchrennew/data-loader-vue3 --skill data-loader-vue3
SKILL.md
DataLoader Vue3 Component Guide

此技能提供关于 DataLoader.vue 组件的详细使用指南。该组件用于简化 Vue 3 中的异步数据加载场景。

核心功能
自动数据加载：组件挂载或 hash 变化时自动触发 loadData。
错误处理：自动捕获异常并显示错误信息。
数据过滤：支持 filter 函数处理数据。
状态管理：管理 loading 和 data 状态。
使用场景
1. 新功能开发 (/use loader)

当用户输入 /use loader 或询问如何使用时，参考此部分。

引入组件
import DataLoader from 'data-loader-vue3';

基本使用
<template>
  <DataLoader
    :hash="queryParams"
    :load-data="fetchData"
    :load-data-args="queryParams"
    :filter="dataFilter"
    #="{ filteredData, reload, data }"
  >
    <div v-if="!filteredData">Loading...</div>
    <div v-else>
      <!-- 使用数据 -->
      <div v-for="item in filteredData" :key="item.id">
          {{ item.name }}
      </div>
      <button @click="reload(false)">重新加载</button>
    </div>
  </DataLoader>
</template>

<script setup>
import { ref } from 'vue';
import DataLoader from 'data-loader-vue3';

const queryParams = ref({ page: 1 });

const fetchData = async (args) => {
  // 模拟 API 调用
  return await api.getData(args);
};

const dataFilter = (data) => {
  // 可选：过滤数据
  return data.list;
};
</script>

2. 代码重构 (/migrate loader)

当用户输入 /migrate loader 或询问如何优化旧代码时，参考此部分。当遇到使用 watch、onMounted 或手动管理 loading 状态的传统代码时，应推荐重构为 DataLoader。

重构前 (Traditional)
<script setup>
import { ref, watch, onMounted } from 'vue';

const data = ref([]);
const loading = ref(false);
const error = ref(null);
const params = ref({ id: 1 });

const fetchData = async () => {
  loading.value = true;
  error.value = null;
  try {
    data.value = await api.get(params.value);
  } catch (e) {
    error.value = e;
  } finally {
    loading.value = false;
  }
};

onMounted(fetchData);

watch(params, fetchData, { deep: true });
</script>

<template>
  <div v-if="loading">Loading...</div>
  <div v-else-if="error">{{ error.message }}</div>
  <ul v-else>
    <li v-for="item in data" :key="item.id">{{ item.name }}</li>
  </ul>
</template>

重构后 (With DataLoader)
移除：loading、error 状态变量，onMounted，watch。
保留：数据获取逻辑 (fetchData) 和参数 (params)。
新增：DataLoader 组件包裹。
<script setup>
import { ref } from 'vue';
import DataLoader from 'data-loader-vue3';

const params = ref({ id: 1 });

// 仅需关注数据获取，无需管理 loading/error
const fetchData = async (args) => await api.get(args);
</script>

<template>
  <!-- hash 变化自动触发重新加载 -->
  <DataLoader :hash="params" :load-data="fetchData" :load-data-args="params" #="{ data }">
    <ul>
      <li v-for="item in data" :key="item.id">{{ item.name }}</li>
    </ul>
  </DataLoader>
</template>

重构收益
代码量减少：移除了手动状态管理和生命周期钩子。
逻辑解耦：UI 状态（加载中/错误）由组件统一处理，业务逻辑只关注数据获取。
竞态处理：DataLoader 内部通过 hash 校验自动处理了请求竞态问题。
API 参考
Props
属性名	类型	必填	默认值	说明
hash	Any	是	-	数据版本标识，变化时触发重载
loadData	Function	是	-	异步加载函数，需返回 Promise
loadDataArgs	Any	否	undefined	传给 loadData 的参数
filter	Function	否	undefined	数据过滤器函数
reloaderName	String	否	'reload'	注入（Provide）给子组件的重载函数名称
Events
loaded(data, hash, filteredData): 数据加载成功时触发
Dependency Injection

组件通过 provide 向下提供重载函数，子组件可以通过 inject(reloaderName) 获取。

Default Key: 'reload'
Value: (loaded: any) => void (同 slot 中的 reload 函数)
Slots (Default)

默认插槽提供以下属性（Scoped Props）：

data: 原始数据
filtered-data: 经过 filter 处理后的数据（如果没有 filter 则等于 data）
loaded: 当前数据是否匹配 hash (Boolean)
reload($loaded: any): 重新加载/设置状态函数。调用 reload(false) 可强制刷新。
注意事项
错误处理: loadData 中的任何抛出异常都会被捕获并显示为错误提示。
响应式: 修改 hash 属性会自动触发重新加载，无需手动调用 reload。
Weekly Installs
11
Repository
lchrennew/data-…der-vue3
GitHub Stars
1
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass