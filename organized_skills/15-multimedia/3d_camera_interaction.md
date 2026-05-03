---
rating: ⭐⭐
title: 3d-camera-interaction
url: https://skills.sh/project-n-e-k-o/n.e.k.o/3d-camera-interaction
---

# 3d-camera-interaction

skills/project-n-e-k-o/n.e.k.o/3d-camera-interaction
3d-camera-interaction
Installation
$ npx skills add https://github.com/project-n-e-k-o/n.e.k.o --skill 3d-camera-interaction
SKILL.md
3D 相机交互：拖拽与边界检测
症状
缩放后拖拽模型，鼠标移动 100px 但模型移动的屏幕距离不是 100px
放大模型后只能看到腿/身体的一部分，无法正常平移
拖动开始时模型位置"跳变"
根本原因
原因 1: 固定 panSpeed 导致移动不同步

问题: 使用固定的 panSpeed = 0.01 进行平移计算

// ❌ 错误方式
const panSpeed = 0.01;
newPosition.add(right.multiplyScalar(deltaX * panSpeed));


为什么发生: 相机距离变化时，同样的世界空间距离在屏幕上的像素表现不同。距离近时像素多，距离远时像素少。

解决方案: 根据相机距离和 FOV 动态计算像素→世界空间的映射

// ✅ 正确方式：动态计算
const cameraDistance = camera.position.distanceTo(modelCenter);
const fov = camera.fov * (Math.PI / 180);
const screenHeight = renderer.domElement.clientHeight;
const screenWidth = renderer.domElement.clientWidth;

// 在相机距离处，视口的世界空间高度
const worldHeight = 2 * Math.tan(fov / 2) * cameraDistance;
const worldWidth = worldHeight * (screenWidth / screenHeight);

// 每像素对应的世界空间距离
const pixelToWorldX = worldWidth / screenWidth;
const pixelToWorldY = worldHeight / screenHeight;

// 应用：鼠标移动的像素 × 每像素对应的世界空间距离
newPosition.add(right.multiplyScalar(deltaX * pixelToWorldX));
newPosition.add(up.multiplyScalar(-deltaY * pixelToWorldY));

原因 2: 基于中心点的边界限制

问题: 使用模型中心点的 NDC 坐标判断是否出界

// ❌ 错误方式：限制中心点位置
const ndc = position.clone().project(camera);
if (ndc.y > 0.2) clampedY = 0.2; // 限制顶部


为什么发生: 模型放大后，中心点在屏幕中心，但身体大部分已超出屏幕。限制中心点 = 限制只能看到身体中间部分。

解决方案: 计算模型在屏幕上的可见区域（像素），只在可见区域过小时才校正

// ✅ 正确方式：基于可见像素
const MIN_VISIBLE_PIXELS = 50;

// 1. 计算模型包围盒并投影到屏幕
const box = new THREE.Box3().setFromObject(vrm.scene);
const corners = [/* 8个顶点 */];

let modelMinX = Infinity, modelMaxX = -Infinity;
let modelMinY = Infinity, modelMaxY = -Infinity;

corners.forEach(corner => {
    const projected = corner.clone().project(camera);
    const screenX = (projected.x * 0.5 + 0.5) * screenWidth;
    const screenY = (-projected.y * 0.5 + 0.5) * screenHeight;
    // 更新边界...
});

// 2. 计算可见区域
const visibleWidth = Math.max(0, Math.min(screenWidth, modelMaxX) - Math.max(0, modelMinX));
const visibleHeight = Math.max(0, Math.min(screenHeight, modelMaxY) - Math.max(0, modelMinY));
const visiblePixels = visibleWidth * visibleHeight;

// 3. 只在可见区域太小时校正
if (visiblePixels < MIN_VISIBLE_PIXELS) {
    // 将模型拉回可见区域
}

关键公式
像素到世界空间转换
worldHeight = 2 × tan(fov/2) × cameraDistance
pixelToWorld = worldHeight / screenHeight

世界坐标到屏幕坐标
const ndc = worldPos.clone().project(camera);
const screenX = (ndc.x * 0.5 + 0.5) * screenWidth;
const screenY = (-ndc.y * 0.5 + 0.5) * screenHeight; // Y 轴反向

关键经验
📐 相机距离影响一切: 所有像素↔世界空间的转换都需要考虑相机距离
🔲 使用包围盒而非中心点: 边界检测应基于模型实际占用的屏幕区域
🔄 与 2D 保持一致: Live2D/VRM 等不同类型模型应使用相同的交互逻辑阈值
Weekly Installs
61
Repository
project-n-e-k-o/n.e.k.o
GitHub Stars
995
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass