Name:		gwenview
Summary:	Fast and easy to use image viewer for KDE
Version:	4.8.97
Release:	2
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		gwenview-4.8.3-drop-inode-directory.patch
BuildRequires:	kdebase4-devel
BuildRequires:	pkgconfig(exiv2)
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

#------------------------------------------------

%define gwenviewlib_major 4
%define libgwenviewlib %mklibname gwenviewlib %{gwenviewlib_major}

%package -n %{libgwenviewlib}
Summary:	Gwenview library
Group:		System/Libraries

%description -n %{libgwenviewlib}
Gwenview library.

%files -n %{libgwenviewlib}
%{_kde_libdir}/libgwenviewlib.so.%{gwenviewlib_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libgwenviewlib} = %{EVRD}
Requires:	pkgconfig(libkipi)
Conflicts:	kdegraphics4-devel < 2:4.6.90

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde_libdir}/libgwenviewlib.so

#----------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

