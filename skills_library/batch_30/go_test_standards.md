---
title: go-test-standards
url: https://skills.sh/iceleaf916/my-cc-plugins/go-test-standards
---

# go-test-standards

skills/iceleaf916/my-cc-plugins/go-test-standards
go-test-standards
Installation
$ npx skills add https://github.com/iceleaf916/my-cc-plugins --skill go-test-standards
SKILL.md
Golang 单元测试规范
一、需要遵循的单元测试理论
1.1 每个测试单元逻辑上分为四个阶段(可以用阶段名作为注释分割)
阶段	说明
Setup	准备测试所需的数据和环境
Exercise	执行被测试的代码
Verify	验证执行结果是否符合预期
Teardown	清理测试环境和数据
1.2 测试替身使用原则
尽可能使用 stub 类型，而不是 mock。为 stub 对象命名时应带有 stub 关键字而不是 mock关键字。
针对全局函数的模拟考虑使用 monkey patching
二、单测代码规范
2.1 框架与断言库

Go 项目必须使用以下工具：

ginkgo - BDD 测试框架
gomega - 断言库

注意事项：

ginkgo 可以使用 . 导入。gomega 不要使用 . 导入，而且禁止使用 Ω 别名。
测试套件注册入口单独写到 suite_test.go。
被测试文件包为 abc，则测试文件属于 abc_test 包。
2.2 数据访问层测试模板
package db_test

import (
    "fmt"
    "reflect"
    "testing"

    _ "github.com/go-sql-driver/mysql"
    "github.com/jinzhu/gorm"
    . "github.com/onsi/ginkgo/v2"
    . "github.com/onsi/gomega"
    dockertest "github.com/ory/dockertest/v3"
    "github.com/ory/dockertest/v3/docker"
)

const (
    dbName = "test"
    dbPwd  = "test"
)

func TestDB(t *testing.T) {
    RegisterFailHandler(Fail)
    RunSpecs(t, "Db Test Suite", Label("repo", "store/db"))
}

var (
    Db            *gorm.DB
    cleanupDocker func()
)

var _ = BeforeSuite(func() {
    Db, cleanupDocker = setupGormWithDocker()
})

var _ = AfterSuite(func() {
    cleanupDocker()
})

var _ = BeforeEach(func() {
    Except(cleanDatabase(Db, dbName)).To(Succeed())
})

func setupGormWithDocker() (*gorm.DB, func()) {
    pool, err := dockertest.NewPool("")
    chk(err)

    runDockerOpt := &dockertest.RunOptions{
        Repository: "hub.deepin.com/library/mariadb",
        Tag:        "10.3.35",
        Env:        []string{"MARIADB_DATABASE=" + dbName, "MARIADB_ROOT_PASSWORD=" + dbPwd},
    }

    fnConfig := func(config *docker.HostConfig) {
        config.AutoRemove = true
        config.RestartPolicy = docker.NeverRestart()
    }

    resource, err := pool.RunWithOptions(runDockerOpt, fnConfig)
    chk(err)

    fnCleanup := func() {
        err := resource.Close()
        chk(err)
    }

    dsn := fmt.Sprintf("root:%s@tcp(localhost:%s)/%s?charset=utf8&parseTime=True&loc=Local",
        dbPwd,
        resource.GetPort("3306/tcp"),
        dbName,
    )

    var gdb *gorm.DB
    err = pool.Retry(func() error {
        gdb, err = gorm.Open("mysql", dsn)
        if err != nil {
            return err
        }
        return gdb.DB().Ping()
    })
    chk(err)

    return gdb, fnCleanup
}

func cleanDatabase(db *gorm.DB, dbName string) error {
    // 删除数据库内的所有对象，比如数据表，以达到重置数据库的作用
}

func chk(err error) {
    if err != nil {
        panic(err)
    }
}

三、单元测试工具库
3.1 Framework
工具	说明
ginkgo	Expressive BDD testing framework with Gomega matchers
gomega	Ginkgo's Preferred Matcher Library
biloba	Stable, performant, automated browser testing for Ginkgo
chromedp	Drive Chrome browsers via DevTools Protocol
3.2 Integration
工具	说明
iotest	Std Package - Readers and Writers for testing
httptest	Std Package - HTTP testing utilities
dockertest	Run integration tests with Docker containers
testcontainers-go	Programmatically manage Docker containers
3.3 Double (Test Doubles)
工具	类型	说明
moq	Stub	Generate interface mocks for testing
gomonkey	Monkey	Monkey patching library for unit testing
mock	Mock	Go mocking framework with code generation
Weekly Installs
11
Repository
iceleaf916/my-cc-plugins
GitHub Stars
6
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass