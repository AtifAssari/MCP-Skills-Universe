---
rating: ⭐⭐
title: unity-package
url: https://skills.sh/besty0728/unity-skills/unity-package
---

# unity-package

skills/besty0728/unity-skills/unity-package
unity-package
Installation
$ npx skills add https://github.com/besty0728/unity-skills --skill unity-package
SKILL.md
Package Skills

Manage installed Unity packages and package-related helper flows such as Cinemachine and Splines setup.

Guardrails

Mode: Full-Auto required

DO NOT (common hallucinations):

package_add / package_update do not exist -> use package_install
package_get_info does not exist -> use package_list, package_check, package_get_dependencies, or package_get_versions
package_search searches the installed package cache only; it does not query the Unity Registry
package_list, package_search, package_get_dependencies, and package_get_versions can return "Package list not ready" until package_refresh completes
Package install/remove/refresh jobs can trigger package import and Domain Reload; expect transient server unavailability and use returned job IDs

Routing:

For Cinemachine quick setup -> use package_install_cinemachine
For Splines quick setup -> use package_install_splines
For project manifest inspection -> use project_get_packages
For define symbol changes after package installation -> use debug_set_defines
Skills
package_list

List all installed packages currently cached by UnitySkills. Parameters: None.

Returns: { success, count, packages }

package_check

Check whether a package is installed.

Parameter	Type	Required	Default	Description
packageId	string	Yes	-	Package ID such as com.unity.cinemachine

Returns: { packageId, installed, version }

package_install

Install a package. Returns an async job when the request is accepted.

Parameter	Type	Required	Default	Description
packageId	string	Yes	-	Package ID to install
version	string	No	null	Optional explicit version

Returns: { success, status, jobId, message, serverAvailability }

package_remove

Remove an installed package. Returns an async job when the request is accepted.

Parameter	Type	Required	Default	Description
packageId	string	Yes	-	Installed package ID to remove

Returns: { success, status, jobId, message, serverAvailability }

package_refresh

Refresh the installed package cache used by query skills. Parameters: None.

Returns: { success, status, jobId, message }

package_install_cinemachine

Install Cinemachine using the supported package/version strategy.

Parameter	Type	Required	Default	Description
version	int	No	3	2 for CM2, 3 for CM3

Notes:

CM3 auto-installs the Splines dependency.
If the requested line is already installed, this skill can return immediate success instead of a job.

Returns: { success, status?, jobId?, message, serverAvailability? }

package_install_splines

Install or upgrade Unity Splines using the recommended version for the current Unity editor line. Parameters: None.

Returns: { success, status?, jobId?, message, serverAvailability? }

package_get_cinemachine_status

Get current Cinemachine and Splines installation status. Parameters: None.

Returns: { cinemachine, splines }

package_search

Search the installed package cache by package name or display name.

Parameter	Type	Required	Default	Description
query	string	Yes	-	Search keyword

Returns: { success, query, count, packages }

package_get_dependencies

Get dependency information for one installed package.

Parameter	Type	Required	Default	Description
packageId	string	Yes	-	Installed package ID

Returns: { success, packageId, version, dependencyCount, dependencies }

package_get_versions

Get available versions for one installed package.

Parameter	Type	Required	Default	Description
packageId	string	Yes	-	Installed package ID

Returns: { success, packageId, currentVersion, compatibleVersion, latestVersion, allVersions }

Exact Signatures

Exact names, parameters, defaults, and returns are defined by GET /skills/schema or unity_skills.get_skill_schema(), not by this file.

Weekly Installs
14
Repository
besty0728/unity-skills
GitHub Stars
894
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass