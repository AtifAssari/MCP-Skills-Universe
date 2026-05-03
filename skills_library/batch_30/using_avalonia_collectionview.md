---
title: using-avalonia-collectionview
url: https://skills.sh/christian289/dotnet-with-claudecode/using-avalonia-collectionview
---

# using-avalonia-collectionview

skills/christian289/dotnet-with-claudecode/using-avalonia-collectionview
using-avalonia-collectionview
Installation
$ npx skills add https://github.com/christian289/dotnet-with-claudecode --skill using-avalonia-collectionview
SKILL.md
6.7 MVVM Pattern with CollectionView

⚠️ Important: AvaloniaUI does not support WPF's CollectionViewSource.

Project Structure

The templates folder contains a .NET 9 AvaloniaUI project example.

templates/
├── AvaloniaCollectionViewSample.Core/           ← Pure C# models and interfaces
│   ├── Member.cs
│   ├── IMemberCollectionService.cs
│   └── AvaloniaCollectionViewSample.Core.csproj
├── AvaloniaCollectionViewSample.ViewModels/     ← ViewModel (no Avalonia references)
│   ├── MainViewModel.cs
│   ├── GlobalUsings.cs
│   └── AvaloniaCollectionViewSample.ViewModels.csproj
├── AvaloniaCollectionViewSample.AvaloniaServices/ ← Avalonia Service Layer
│   ├── MemberCollectionService.cs
│   ├── GlobalUsings.cs
│   └── AvaloniaCollectionViewSample.AvaloniaServices.csproj
└── AvaloniaCollectionViewSample.App/            ← Avalonia Application
    ├── Views/
    │   ├── MainWindow.axaml
    │   └── MainWindow.axaml.cs
    ├── App.axaml
    ├── App.axaml.cs
    ├── Program.cs
    ├── GlobalUsings.cs
    └── AvaloniaCollectionViewSample.App.csproj


In AvaloniaUI, use the following approaches:

6.7.1 Using DataGridCollectionView (Recommended)
// NuGet: Avalonia.Controls.DataGrid
// Service Layer
namespace MyApp.Services;

using Avalonia.Controls;

public sealed class MemberCollectionService
{
    private ObservableCollection<Member> Source { get; } = [];

    // Returns DataGridCollectionView
    public IEnumerable CreateView(Predicate<Member>? filter = null)
    {
        var view = new DataGridCollectionView(Source);

        if (filter is not null)
        {
            view.Filter = item => filter((Member)item);
        }

        return view;
    }

    public void Add(Member item) => Source.Add(item);
    public void Remove(Member? item) { if (item is not null) Source.Remove(item); }
    public void Clear() => Source.Clear();
}

6.7.2 Using ReactiveUI (Alternative)
// NuGet: ReactiveUI.Avalonia
namespace MyApp.ViewModels;

using ReactiveUI;
using DynamicData;

public sealed class MainViewModel : ReactiveObject
{
    private readonly SourceList<Member> _sourceList = new();
    private readonly ReadOnlyObservableCollection<Member> _members;

    public ReadOnlyObservableCollection<Member> Members => _members;

    public MainViewModel()
    {
        _sourceList
            .Connect()
            .Filter(m => m.IsActive) // Filtering
            .Sort(SortExpressionComparer<Member>.Ascending(m => m.Name)) // Sorting
            .Bind(out _members)
            .Subscribe();
    }

    public void AddMember(Member member) => _sourceList.Add(member);
    public void RemoveMember(Member member) => _sourceList.Remove(member);
}

Weekly Installs
9
Repository
christian289/do…audecode
GitHub Stars
28
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass