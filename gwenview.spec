Summary:	Fast and easy to use image viewer for KDE
Name:		gwenview
Epoch:		2
Version:	4.10.3
Release:	2
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
# Drop inode/directory, add image/svg+xml and image/svg+xml-compressed
Patch0:		gwenview-4.10.1-mimetypes.patch
# Revert https://projects.kde.org/projects/kde/kdegraphics/gwenview/repository/revisions/fe4b195b2023aeae92a58188a4578c1c6b08db86
# because it breaks image rotation
Patch1:		gwenview-4.10.2-fix-rotate.patch
BuildRequires:	kdebase4-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(libkipi)
Requires:	kipi-common

%description
Gwenview is a fast and easy to use image viewer/browser for KDE.
All common image formats are supported, such as PNG(including transparency),
JPEG(including EXIF tags and lossless transformations), GIF, XCF (Gimp
image format), BMP, XPM and others. Standard features include slideshow,
fullscreen view, image thumbnails, drag'n'drop, image zoom, full network
transparency using the KIO framework, including basic file operations and
browsing in compressed archives, non-blocking GUI with adjustable views.
Gwenview also provides image and directory KParts components for use e.g. in
Konqueror. Additional features, such as image renaming, comparing,
converting, and batch processing, HTML gallery and others are provided by the
KIPI image framework.

%files
%doc %{_kde_docdir}/HTML/en/gwenview/
%{_kde_bindir}/gwenview
%{_kde_bindir}/gwenview_importer
%{_kde_libdir}/kde4/gvpart.so
%{_kde_appsdir}/gvpart
%{_kde_appsdir}/gwenview
%{_kde_services}/gvpart.desktop
%{_kde_services}/ServiceMenus/slideshow.desktop
%{_kde_applicationsdir}/gwenview.desktop
%{_kde_appsdir}/solid/actions/gwenview_importer.desktop
%{_kde_appsdir}/solid/actions/gwenview_importer_camera.desktop
%{_kde_iconsdir}/*/*/*/gwenview*
%{_kde_iconsdir}/*/*/*/document-share*

%define major 4
%define libgwenviewlib %mklibname gwenviewlib %{major}
%define devgwenviewlib %mklibname gwenviewlib -d

%package -n %{libgwenviewlib}
Summary:	Gwenview library
Group:		System/Libraries

%description -n %{libgwenviewlib}
Gwenview library.

%files -n %{libgwenviewlib}
%{_kde_libdir}/libgwenviewlib.so.%{major}*

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libgwenviewlib} = %{EVRD}
Conflicts:	kdegraphics4-devel < 2:4.6.90
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	gwenview-devel < 2:4.10.3-2

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde_libdir}/libgwenviewlib.so

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

