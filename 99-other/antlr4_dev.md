---
title: antlr4-dev
url: https://skills.sh/whtoo/how_to_implment_pl_in_antlr4/antlr4-dev
---

# antlr4-dev

skills/whtoo/how_to_implment_pl_in_antlr4/antlr4-dev
antlr4-dev
Installation
$ npx skills add https://github.com/whtoo/how_to_implment_pl_in_antlr4 --skill antlr4-dev
SKILL.md
ANTLR4前端开发
🎯 垂直职责

单一职责: ANTLR4语法设计、词法/语法分析、AST构建、访问者模式

📦 核心能力
1. 语法文件开发
位置: ep20/src/main/antlr4/org/teachfx/antlr4/ep20/parser/Cymbol.g4
语法结构: lexer规则 → parser规则 → AST构建
重新生成: mvn generate-sources -pl ep20
2. AST节点实现
基类: ASTNode.java (位于 ep20/src/main/java/org/teachfx/antlr4/ep20/ast/)
模式: 访问者模式 accept(ASTVisitor<T>)
扩展: 创建新节点继承 ExprNode / StmtNode
3. 访问者模式
// 新节点标准实现
public class NewStmtNode extends StmtNode {
    private final Type field;

    public NewStmtNode(Type field) {
        this.field = field;
    }

    @Override
    public <T> T accept(ASTVisitor<T> visitor) {
        return visitor.visitNewStmt(this);
    }
}

🔗 关系图

→ ep-navigator (识别EP范围) ← compiler-dev (AST → IR转换)

🚀 快速开始
添加新语法特性
# 1. 编辑 Cymbol.g4
vim ep20/src/main/antlr4/.../parser/Cymbol.g4

# 2. 重新生成解析器
mvn generate-sources -pl ep20

# 3. 创建AST节点
vim ep20/src/main/java/.../ast/NewNode.java

# 4. 更新AST构建器
vim ep20/src/main/java/.../pass/ast/CymbolASTBuilder.java

# 5. 测试
mvn test -pl ep20 -Dtest="*ParserTest"

调试语法冲突
# 使用TestRig可视化语法树
java -cp "antlr-4.13.2-complete.jar:ep20/target/classes" \
  org.antlr.v4.gui.TestRig Cymbol file -gui test.cymbol

# 诊断冲突
mvn generate-sources -pl ep20 -Xantlr4.show-dfa

📚 Cymbol语法速查
类型	规则	示例
变量声明	declaration	int x;
函数定义	functionDef	int add(int a, int b) { ... }
结构体	structDef	struct Point { int x; int y; }
数组	type '[' expr? ']'	int[10] arr;
控制流	ifStmt / whileStmt	if (x > 0) { ... }
🛠️ 常用命令
# 语法相关
mvn generate-sources -pl ep20              # 重新生成解析器
mvn test -pl ep20 -Dtest="*Lexer*"         # 测试词法
mvn test -pl ep20 -Dtest="*Parser*"        # 测试语法

# AST相关
mvn test -pl ep20 -Dtest="*AST*"           # 测试AST构建
mvn test -pl ep20 -Dtest="*Visitor*"       # 测试访问者

# 完整前端
mvn compile -pl ep20 && mvn test -pl ep20  # 编译并测试前端

⚠️ 常见问题
问题	原因	解决方案
语法冲突	左递归/歧义	重构规则，使用语义谓词
AST未生成	忘记运行generate-sources	mvn generate-sources -pl ep20
访问者空指针	新节点未实现accept()	添加 accept(ASTVisitor<T>)

版本: v1.0 | 垂直职责: ANTLR4前端 | 2025-12-23

Weekly Installs
8
Repository
whtoo/how_to_im…n_antlr4
GitHub Stars
33
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass