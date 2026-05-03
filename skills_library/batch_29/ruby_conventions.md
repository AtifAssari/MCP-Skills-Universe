---
title: ruby-conventions
url: https://skills.sh/phrazzld/claude-config/ruby-conventions
---

# ruby-conventions

skills/phrazzld/claude-config/ruby-conventions
ruby-conventions
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill ruby-conventions
SKILL.md
Ruby Conventions

Service objects, strong params, behavior-focused tests.

Architecture

Service objects for business logic:

# app/services/user_registration_service.rb
class UserRegistrationService
  def initialize(user_params:, mailer: UserMailer)
    @user_params = user_params
    @mailer = mailer
  end

  def call
    user = User.create!(@user_params)
    @mailer.welcome(user).deliver_later
    user
  end
end


Thin controllers:

def create
  user = UserRegistrationService.new(user_params: user_params).call
  render json: UserSerializer.new(user), status: :created
rescue ActiveRecord::RecordInvalid => e
  render json: { errors: e.record.errors }, status: :unprocessable_entity
end

Strong Parameters

Always use strong params. Never mass-assign directly:

# Good
def user_params
  params.require(:user).permit(:email, :name, :password)
end

# Never
User.create(params[:user])  # SQL injection risk

Query Safety

Always parameterize queries:

# Good
User.where(email: email)
User.where("email = ?", email)

# Never
User.where("email = '#{email}'")  # SQL injection


Prevent N+1 queries:

# Good
User.includes(:posts).each { |u| u.posts.count }

# Bad (N+1)
User.all.each { |u| u.posts.count }

Testing with RSpec
RSpec.describe UserRegistrationService do
  describe "#call" do
    it "creates active user with welcome email" do
      mailer = instance_double(UserMailer)
      allow(mailer).to receive(:welcome).and_return(double(deliver_later: true))

      service = described_class.new(
        user_params: { email: "test@example.com", name: "Test" },
        mailer: mailer
      )

      user = service.call

      expect(user).to be_persisted
      expect(user.email).to eq("test@example.com")
      expect(mailer).to have_received(:welcome).with(user)
    end
  end
end


Use FactoryBot, not fixtures:

FactoryBot.define do
  factory :user do
    email { Faker::Internet.email }
    name { Faker::Name.name }
  end
end

let(:user) { create(:user) }

API Design
# Consistent serialization
class UserSerializer
  include JSONAPI::Serializer
  attributes :id, :email, :name, :created_at
end

# Versioned routes
namespace :api do
  namespace :v1 do
    resources :users
  end
end

Language Patterns
# Keyword arguments for 2+ params
def send_email(to:, subject:, body:)
  ...
end

# Safe navigation
user&.profile&.avatar_url

# Frozen strings (file header)
# frozen_string_literal: true

Anti-Patterns
Fat models (business logic in ActiveRecord)
Business logic in controllers
Fixtures instead of factories
Testing implementation (mocking internals)
String interpolation in SQL
N+1 queries without includes
Synchronous email in request cycle
References
rails-performance.md - Caching, background jobs, profiling
Weekly Installs
25
Repository
phrazzld/claude-config
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass