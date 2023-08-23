%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Fast and easy to use image viewer for KDE
Name:		gwenview
Version:	23.08.0
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(KF5Baloo)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5KDcraw)
BuildRequires:	cmake(KF5Kipi)
BuildRequires:	cmake(KF5Purpose)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(kImageAnnotator)
BuildRequires:	cmake(WaylandProtocols)
BuildRequires:	pkgconfig(wayland-protocols)
Requires:	kipi-common
Requires:	kinit
Requires:	kio-extras

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

%files -f gwenview.lang
%{_bindir}/gwenview
%{_bindir}/gwenview_importer
%{_datadir}/applications/*gwenview.desktop
%{_datadir}/applications/org.kde.gwenview_importer.desktop
%{_datadir}/metainfo/org.kde.gwenview.appdata.xml
%{_datadir}/kconf_update/gwenview.upd
%{_datadir}/kconf_update/gwenview-imageview-alphabackgroundmode-update.pl
%{_datadir}/gwenview
%{_datadir}/solid/actions/gwenview*.desktop
%{_datadir}/kservices5/gvpart.desktop
%{_libdir}/qt5/plugins/kf5/parts/gvpart.so
%{_libdir}/qt5/plugins/kf5/kfileitemaction/slideshowfileitemaction.so
%{_datadir}/qlogging-categories5/gwenview.categories
%{_iconsdir}/*/*/*/gwenview*
%{_iconsdir}/*/*/*/document-share*

#------------------------------------------------

%define gwenviewlib_major 5
%define libgwenviewlib %mklibname gwenviewlib %{gwenviewlib_major}

%package -n %{libgwenviewlib}
Summary:	Gwenview library
Group:		System/Libraries

%description -n %{libgwenviewlib}
Gwenview library.

%files -n %{libgwenviewlib}
%{_libdir}/libgwenviewlib.so.%{gwenviewlib_major}*
%{_libdir}/libgwenviewlib.so.4.97*

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# We don't need this as we don't have any devel headers
rm -f %{buildroot}%{_libdir}/libgwenviewlib.so

%find_lang gwenview --all-name --with-html
