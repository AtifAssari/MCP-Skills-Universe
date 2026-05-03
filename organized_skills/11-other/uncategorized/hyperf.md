---
rating: ⭐⭐⭐
title: hyperf
url: https://skills.sh/fanqingxuan/awesome-skills/hyperf
---

# hyperf

skills/fanqingxuan/awesome-skills/hyperf
hyperf
Installation
$ npx skills add https://github.com/fanqingxuan/awesome-skills --skill hyperf
SKILL.md
Hyperf 3.1 开发指南

Hyperf 3.1 框架开发助手，专注于控制器、模型、命令行工具的快速开发。

常用命令
# 生成控制器
php bin/hyperf.php gen:controller UserController

# 生成模型
php bin/hyperf.php gen:model User

# 生成命令
php bin/hyperf.php gen:command ImportCommand

# 生成中间件
php bin/hyperf.php gen:middleware AuthMiddleware

# 生成请求验证类
php bin/hyperf.php gen:request UserRequest

# 启动服务
php bin/hyperf.php start

快速示例
控制器
<?php
declare(strict_types=1);

namespace App\Controller;

use Hyperf\HttpServer\Annotation\Controller;
use Hyperf\HttpServer\Annotation\GetMapping;

#[Controller(prefix: "/api/users")]
class UserController extends AbstractController
{
    #[GetMapping("")]
    public function index()
    {
        return $this->response->json(['code' => 0, 'data' => []]);
    }
}

模型
<?php
declare(strict_types=1);

namespace App\Model;

use Hyperf\DbConnection\Model\Model;

class User extends Model
{
    protected ?string $table = 'users';
    protected array $fillable = ['name', 'email'];
}

命令
<?php
declare(strict_types=1);

namespace App\Command;

use Hyperf\Command\Command as HyperfCommand;
use Hyperf\Command\Annotation\Command;

#[Command]
class ImportDataCommand extends HyperfCommand
{
    protected ?string $name = 'import:data';

    public function handle()
    {
        $this->info('Processing...');
    }
}

服务类
<?php
declare(strict_types=1);

namespace App\Service;

use App\Model\User;

class UserService
{
    public function create(array $data): User
    {
        return User::create($data);
    }
}

官方文档参考

详细文档请参考 references/zh-cn/ 目录下的官方文档：

控制器: references/zh-cn/controller.md
模型: references/zh-cn/db/model.md
命令行: references/zh-cn/command.md
路由: references/zh-cn/router.md
验证器: references/zh-cn/validation.md
依赖注入: references/zh-cn/di.md
Weekly Installs
13
Repository
fanqingxuan/awe…e-skills
GitHub Stars
19
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykWarn