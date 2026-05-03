---
rating: ⭐⭐
title: mantine-combobox
url: https://skills.sh/mantinedev/skills/mantine-combobox
---

# mantine-combobox

skills/mantinedev/skills/mantine-combobox
mantine-combobox
Installation
$ npx skills add https://github.com/mantinedev/skills --skill mantine-combobox
SKILL.md
Mantine Combobox Skill
Overview

Combobox provides low-level primitives for building any select-like UI. The built-in Select, Autocomplete, and TagsInput components are all built on top of it.

Core Workflow
1. Create the store
const combobox = useCombobox({
  onDropdownClose: () => combobox.resetSelectedOption(),
  onDropdownOpen: () => combobox.selectFirstOption(),
});

2. Render structure
<Combobox store={combobox} onOptionSubmit={handleSubmit}>
  <Combobox.Target>
    <InputBase
      component="button"
      pointer
      rightSection={<Combobox.Chevron />}
      onClick={() => combobox.toggleDropdown()}
    >
      {value || <Input.Placeholder>Pick value</Input.Placeholder>}
    </InputBase>
  </Combobox.Target>
  <Combobox.Dropdown>
    <Combobox.Options>
      {options.map((item) => (
        <Combobox.Option value={item} key={item}>{item}</Combobox.Option>
      ))}
    </Combobox.Options>
  </Combobox.Dropdown>
</Combobox>

3. Handle submit
const handleSubmit = (val: string) => {
  setValue(val);
  combobox.closeDropdown();
};

Target Types
Scenario	Use
Button trigger (no text input)	<Combobox.Target targetType="button">
Input trigger	<Combobox.Target> (default)
Pills + separate input (multi-select)	<Combobox.DropdownTarget> + <Combobox.EventsTarget>
References
references/api.md — Full API: useCombobox options and store, all sub-component props, CSS variables, Styles API selectors
references/patterns.md — Code examples: searchable select, multi-select with pills, groups, custom rendering, clear button, form integration
Weekly Installs
561
Repository
mantinedev/skills
GitHub Stars
40
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass