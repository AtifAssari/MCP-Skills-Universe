---
title: swift-ios-ui
url: https://skills.sh/qunwang6/swift-ios-ui/swift-ios-ui
---

# swift-ios-ui

skills/qunwang6/swift-ios-ui/swift-ios-ui
swift-ios-ui
Installation
$ npx skills add https://github.com/qunwang6/swift-ios-ui --skill swift-ios-ui
SKILL.md
Swift iOS UI Skill

Generate production-quality iOS UIKit code from UI designs, screenshots, or descriptions.

Tech Stack (Always Use These)
Purpose	Library
Layout	SnapKit — Auto Layout DSL
Popups / Toasts	SwiftEntryKit
Image Loading	Kingfisher or SDWebImage
JSON Parsing	SwiftyJSON
Step-by-Step Workflow
0. Understand the Input

The user may provide one of the following — adapt accordingly:

Input type	How to handle
Screenshot / image	Carefully read all visible text, colors, layout, spacing, component types
Figma / Sketch description	Extract component hierarchy, spacing tokens, color styles
Text description	Ask clarifying questions if key details (colors, layout direction, data shape) are missing
No input yet	Ask the user: "Please share a UI screenshot, design spec, or describe the screen you want to build."

⚠️ Do NOT start generating code until you have enough UI information. If the user provides a screenshot, analyze it fully before writing a single line.

1. Analyze the UI

Before writing any code, examine the design and identify:

Screen type: full screen / modal / bottom sheet / popup
Layout structure: navigation bar, scroll view, table/collection view, static views
Components: buttons, labels, images, text fields, cards, cells
Colors: extract hex values from the design (or best-match hex if approximate)
Spacing: margins, padding, gaps between elements
Interactive states: normal / highlighted / disabled / loading / empty / error
2. Plan the Architecture

Choose the right UIKit pattern:

UIViewController + UIScrollView → scrollable content screens
UIViewController + UITableView → list screens
UIViewController + UICollectionView → grid / complex layouts
UIView subclass → reusable components / cells
SwiftEntryKit → popups, toasts, bottom sheets, alerts
3. Generate the Code

Follow all conventions in the Code Conventions section below.

4. Output Structure

For each screen, produce:

Main ViewController or View file
Any custom UITableViewCell / UICollectionViewCell subclasses
Any reusable subviews extracted as separate UIView subclasses
A Model struct/class if JSON data is involved
Code Conventions
File Structure
// MARK: - Properties
// MARK: - Lifecycle
// MARK: - Setup
// MARK: - Layout (SnapKit)
// MARK: - Actions
// MARK: - Data / Network
// MARK: - Helpers

SnapKit Layout Rules
Always call setupUI() and setupConstraints() from viewDidLoad (or init for UIView)
Add subviews in setupUI(), define constraints in setupConstraints()
Never use frame or autoresizingMask — SnapKit only
Write spacing values directly as literals in SnapKit constraints — do NOT define enum Layout or extract values to named constants.
// ✅ Correct SnapKit usage
private func setupConstraints() {
    titleLabel.snp.makeConstraints { make in
        make.top.equalTo(headerView.snp.bottom).offset(16)
        make.leading.trailing.equalToSuperview().inset(16)
    }
    
    confirmButton.snp.makeConstraints { make in
        make.bottom.equalTo(view.safeAreaLayoutGuide).inset(16)
        make.leading.trailing.equalToSuperview().inset(16)
        make.height.equalTo(50)
    }
}

Typography — PingFangSC (Always Use This)

⚠️ Never use .systemFont or raw UIFont(name:) strings — always use .pingFangSC() via the extension below.UIFont+PingFangSC.swift already exists in the project. Do NOT output this extension definition in generated code — just call it directly.

// UIFont+PingFangSC.swift — include this extension in every project
extension UIFont {
    enum PingFangSC: String {
        case ultralight = "PingFangSC-Ultralight"
        case thin       = "PingFangSC-Thin"
        case light      = "PingFangSC-Light"
        case regular    = "PingFangSC-Regular"
        case medium     = "PingFangSC-Medium"
        case semibold   = "PingFangSC-Semibold"
    }

    static func pingFangSC(_ style: PingFangSC, size: CGFloat) -> UIFont {
        return UIFont(name: style.rawValue, size: size) ?? .systemFont(ofSize: size)
    }
}


Usage reference:

Weight	Call	Typical use
Ultralight	.pingFangSC(.ultralight, size: n)	Decorative, large display numbers
Thin	.pingFangSC(.thin, size: n)	Subtle secondary info
Light	.pingFangSC(.light, size: n)	Body text, descriptions
Regular	.pingFangSC(.regular, size: n)	Default body / labels
Medium	.pingFangSC(.medium, size: n)	Emphasized labels, button text
Semibold	.pingFangSC(.semibold, size: n)	Titles, nav bar, headers
// ✅ Correct — always call the extension method
titleLabel.font    = .pingFangSC(.semibold, size: 18)
bodyLabel.font     = .pingFangSC(.regular, size: 14)
priceLabel.font    = .pingFangSC(.medium, size: 16)
subtitleLabel.font = .pingFangSC(.light, size: 13)

// ❌ Never do this
titleLabel.font = .systemFont(ofSize: 18, weight: .semibold)
titleLabel.font = UIFont(name: "PingFangSC-Semibold", size: 18)  // raw string usage forbidden

Colors — UIColor.colorWithHexString (Always Use This)

⚠️ Never use UIColor(hexString:), UIColor(hex:), Hue, or SwiftHEXColors — always use UIColor.colorWithHexString(hex:) via the extension below.UIColor+Hex.swift already exists in the project. Do NOT output this extension definition in generated code — just call it directly.

// UIColor+Hex.swift — include this extension in every project
extension UIColor {
    static func colorWithHexString(hex: String) -> UIColor {
        var hexSanitized = hex.trimmingCharacters(in: .whitespacesAndNewlines)
        hexSanitized = hexSanitized.hasPrefix("#") ? String(hexSanitized.dropFirst()) : hexSanitized

        var rgb: UInt64 = 0
        Scanner(string: hexSanitized).scanHexInt64(&rgb)

        let r = CGFloat((rgb & 0xFF0000) >> 16) / 255.0
        let g = CGFloat((rgb & 0x00FF00) >> 8)  / 255.0
        let b = CGFloat(rgb & 0x0000FF)          / 255.0

        return UIColor(red: r, green: g, blue: b, alpha: 1.0)
    }
}


Usage:

❌ Do NOT define `enum AppColor` or any named color constants — write hex values inline directly.
// ✅ Correct
let primary = UIColor.colorWithHexString(hex: "#007AFF")
let dimmed  = UIColor.colorWithHexString(hex: "#212226").withAlphaComponent(0.5)

// ❌ Never do this
let c1 = UIColor(hexString: "#FF6B35")   // SwiftHEXColors — forbidden
let c2 = UIColor(hex: "#2C3E50")         // SwiftHEXColors — forbidden
let c3 = primary.lighten(byAmount: 0.2)  // Hue — forbidden

Image Loading with Kingfisher
// Basic
imageView.kf.setImage(with: URL(string: urlString))

// With placeholder + options
imageView.kf.setImage(
    with: URL(string: urlString),
    placeholder: UIImage(named: "placeholder"),
    options: [
        .transition(.fade(0.25)),
        .cacheOriginalImage
    ]
)

// Cancel on reuse (in UITableViewCell)
override func prepareForReuse() {
    super.prepareForReuse()
    imageView.kf.cancelDownloadTask()
    imageView.image = nil
}

JSON Parsing with SwiftyJSON
import SwiftyJSON

struct UserModel {
    let id: Int
    let name: String
    let avatar: String
    let score: Double
    
    init(json: JSON) {
        self.id     = json["id"].intValue
        self.name   = json["name"].stringValue
        self.avatar = json["avatar"].stringValue
        self.score  = json["score"].doubleValue
    }
    
    static func list(from json: JSON) -> [UserModel] {
        return json.arrayValue.map { UserModel(json: $0) }
    }
}

Localization — LocalizableManager (Always Use This)

⚠️ Never use hardcoded strings for UI text — always use LocalizableManager.localValue("key").

// ✅ Correct
titleLabel.text = LocalizableManager.localValue("register_email")

// ❌ Never do this
titleLabel.text = "Email"
titleLabel.text = "邮箱"


When generating any UI text, you must also output the corresponding localization keys and translations for all 3 languages.

Output format — one table per file:

Key	English	Simplified Chinese	Traditional Chinese
register_email	"Email"	"邮箱"	"郵箱"

en.lproj/Localizable.strings

"register_email" = "Email";


zh-Hans.lproj/Localizable.strings

"register_email" = "邮箱";


zh-Hant.lproj/Localizable.strings

"register_email" = "郵箱";


Key naming convention:

Pattern	Example
{screen}_{element}	register_email, login_password, profile_save_button
{screen}_title	register_title, cart_title
{screen}_hint_{field}	register_hint_email, login_hint_password
common_{action}	common_confirm, common_cancel, common_save

✅ Keys must be lowercase snake_case. Never reuse keys across unrelated screens.

SwiftEntryKit — Popups & Toasts
Toast / Snackbar
func showToast(message: String, isSuccess: Bool = true) {
    var attributes = EKAttributes.topToast
    attributes.entryBackground = .color(color: EKColor(isSuccess ? AppColor.primary : .systemRed))
    attributes.displayDuration = 2.5
    attributes.shadow = .active(with: .init(color: .black, opacity: 0.2, radius: 6))
    
    let style = EKProperty.LabelStyle(
        font: .pingFangSC(.medium, size: 14),
        color: EKColor(.white)
    )
    let labelContent = EKProperty.LabelContent(text: message, style: style)
    let contentView = EKNoteMessageView(with: labelContent)
    SwiftEntryKit.display(entry: contentView, using: attributes)
}

Center Alert Popup
func showAlertPopup(title: String, message: String, confirmAction: @escaping () -> Void) {
    var attributes = EKAttributes.centerFloat
    attributes.entryBackground = .color(color: EKColor(.white))
    attributes.roundCorners = .all(radius: 16)
    attributes.shadow = .active(with: .init(color: .black, opacity: 0.15, radius: 10))
    attributes.screenInteraction = .absorbTouches
    attributes.entryInteraction = .absorbTouches
    attributes.displayDuration = .infinity
    
    // Build your custom UIView popup, then:
    let popupView = CustomAlertView(title: title, message: message)
    popupView.onConfirm = {
        SwiftEntryKit.dismiss()
        confirmAction()
    }
    SwiftEntryKit.display(entry: popupView, using: attributes)
}

Bottom Sheet ⚠️ Always use this exact configuration
/// Standard bottom sheet — MUST use this attribute setup exactly.
/// popupView is a UIView subclass that self-sizes via its own constraints (height: .intrinsic).
func showBottomSheet(popupView: UIView) {
    var attributes = EKAttributes()
    attributes.position = .bottom
    attributes.displayDuration = .infinity
    attributes.screenBackground = .color(
        color: .init(
            light: UIColor(white: 0, alpha: 0.4),
            dark:  UIColor(white: 0, alpha: 0.4)
        )
    )
    attributes.entryBackground = .clear           // popup view draws its own background
    attributes.screenInteraction = .dismiss        // tap outside to dismiss
    attributes.entryInteraction = .forward         // touches pass through to content
    attributes.scroll = .disabled
    attributes.positionConstraints.size = .init(width: .fill, height: .intrinsic)
    attributes.positionConstraints.safeArea = .overridden  // extend under home indicator
    attributes.positionConstraints.verticalOffset = 0

    SwiftEntryKit.display(entry: popupView, using: attributes)
}

// Dismiss from inside the popup:
// SwiftEntryKit.dismiss()


Rules for the popup UIView:

Draw its own background (white + top rounded corners) — NOT via entryBackground
Use SnapKit so the view's intrinsic height is driven by its own content constraints
Add a bottom padding area to account for home indicator
final class SampleBottomSheetView: UIView {

    // MARK: - UI
    private let containerView: UIView = {
        let v = UIView()
        v.backgroundColor = .white
        v.layer.cornerRadius = 20
        v.layer.maskedCorners = [.layerMinXMinYCorner, .layerMaxXMinYCorner]
        v.clipsToBounds = true
        return v
    }()

    // MARK: - Init
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupUI()
        setupConstraints()
    }
    required init?(coder: NSCoder) { fatalError() }

    // MARK: - Setup
    private func setupUI() {
        backgroundColor = .clear
        addSubview(containerView)
        // add content subviews to containerView...
    }

    private func setupConstraints() {
        containerView.snp.makeConstraints { make in
            make.top.leading.trailing.equalToSuperview()
            // ⚠️ Do NOT pin bottom to superview — let content drive height
        }
        // ...content constraints inside containerView...

        // Safe-area bottom padding (home indicator)
        let bottomPadding: CGFloat = 34
        containerView.snp.makeConstraints { make in
            make.bottom.equalToSuperview().inset(0)
        }
        // Add a spacer view at the bottom of containerView with height 34
    }
}

UITableView / UICollectionView Best Practices
// Cell registration
tableView.register(ProductCell.self, forCellReuseIdentifier: ProductCell.reuseId)

// Cell class template
final class ProductCell: UITableViewCell {
    static let reuseId = "ProductCell"
    
    // MARK: - UI
    private let containerView = UIView()
    private let thumbImageView = UIImageView()
    private let titleLabel = UILabel()
    private let priceLabel = UILabel()
    
    // MARK: - Init
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupUI()
        setupConstraints()
    }
    required init?(coder: NSCoder) { fatalError() }
    
    // MARK: - Setup
    private func setupUI() {
        selectionStyle = .none
        contentView.addSubview(containerView)
        containerView.addSubview(thumbImageView)
        containerView.addSubview(titleLabel)
        containerView.addSubview(priceLabel)
        
        titleLabel.font  = .pingFangSC(.medium, size: 15)
        titleLabel.textColor = UIColor.colorWithHexString(hex: "#2D2F35")
        priceLabel.font  = .pingFangSC(.semibold, size: 16)
        priceLabel.textColor = UIColor.colorWithHexString(hex: "#149D93")
    }
    
    private func setupConstraints() {
        containerView.snp.makeConstraints { make in
            make.edges.equalToSuperview().inset(UIEdgeInsets(top: 8, left: 16, bottom: 8, right: 16))
        }
        thumbImageView.snp.makeConstraints { make in
            make.leading.top.bottom.equalToSuperview()
            make.width.height.equalTo(80)
        }
        titleLabel.snp.makeConstraints { make in
            make.top.equalToSuperview().offset(12)
            make.leading.equalTo(thumbImageView.snp.trailing).offset(12)
            make.trailing.equalToSuperview().inset(12)
        }
        priceLabel.snp.makeConstraints { make in
            make.bottom.equalToSuperview().inset(12)
            make.leading.equalTo(thumbImageView.snp.trailing).offset(12)
        }
    }
    
    // MARK: - Configure
    func configure(with model: ProductModel) {
        titleLabel.text = model.name
        priceLabel.text = "¥\(model.price)"
        thumbImageView.kf.setImage(with: URL(string: model.imageUrl), placeholder: UIImage(named: "placeholder"))
    }
    
    override func prepareForReuse() {
        super.prepareForReuse()
        thumbImageView.kf.cancelDownloadTask()
        thumbImageView.image = nil
    }
}

Navigation Bar Customization
private func setupNavigationBar() {
    title = "Page Title"
    navigationController?.navigationBar.tintColor = AppColor.primary
    navigationController?.navigationBar.titleTextAttributes = [
        .foregroundColor: AppColor.text,
        .font: UIFont.pingFangSC(.semibold, size: 17)
    ]
    // Right bar button
    let rightBtn = UIBarButtonItem(image: UIImage(systemName: "bell"), 
                                   style: .plain, 
                                   target: self, 
                                   action: #selector(rightButtonTapped))
    navigationItem.rightBarButtonItem = rightBtn
}

Empty State & Loading State
// Loading
func showLoading() {
    let indicator = UIActivityIndicatorView(style: .medium)
    indicator.tag = 999
    indicator.startAnimating()
    view.addSubview(indicator)
    indicator.snp.makeConstraints { $0.center.equalToSuperview() }
}

func hideLoading() {
    view.viewWithTag(999)?.removeFromSuperview()
}

// Empty state
func showEmptyState(message: String = "暂无数据") {
    let label = UILabel()
    label.text = message
    label.textColor = AppColor.subtext
    label.font = .pingFangSC(.regular, size: 15)
    label.tag = 998
    view.addSubview(label)
    label.snp.makeConstraints { $0.center.equalToSuperview() }
}

Output Checklist

Before finishing, verify:

 No frame / AutoresizingMask usage — SnapKit only
 All fonts use .pingFangSC() extension — never .systemFont or raw UIFont(name:) strings
 Safe area insets handled (safeAreaLayoutGuide)
 All colors use UIColor.colorWithHexString(hex:) inline — no AppColor enum, never Hue or SwiftHEXColors
 Images use kf.setImage with placeholder
 prepareForReuse cancels Kingfisher tasks in cells
 JSON models use SwiftyJSON with init(json: JSON)
 Popups use SwiftEntryKit (no UIAlertController unless truly native alert)
 All UI created programmatically (no Storyboard/XIB unless asked)
 // MARK: sections used for code organization
 Spacing values written as inline literals — no enum Layout
 Bottom sheets use the exact EKAttributes config from the Bottom Sheet section (never EKAttributes.bottomFloat)
 Bottom sheet popup view sets entryBackground = .clear and draws its own background
 Bottom sheet config includes safeArea = .overridden and verticalOffset = 0
 Do NOT output extension UIFont or extension UIColor definitions — these extensions already exist in the project
 All UI strings use LocalizableManager.localValue("key") — no hardcoded text
 Localization keys follow {screen}_{element} naming convention
 All 3 language translations are output alongside the code: en, zh-Hans, zh-Hant
Weekly Installs
19
Repository
qunwang6/swift-ios-ui
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass