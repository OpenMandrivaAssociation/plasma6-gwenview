%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Fast and easy to use image viewer for KDE
Name:		plasma6-gwenview
Version:	24.12.3
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://www.kde.org
%if 0%{?git}
Source0:	https://invent.kde.org/graphics/gwenview/-/archive/%{gitbranch}/gwenview-%{gitbranchd}.tar.bz2#/gwenview-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/gwenview-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	cmake(WaylandProtocols)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(KF6Baloo)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(PlasmaActivities)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Purpose)
BuildRequires:	%mklibname -d KF6IconWidgets
BuildRequires:	cmake(KDcrawQt6)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(WaylandProtocols)
BuildRequires:	cmake(kImageAnnotator-Qt6)
BuildRequires:	cmake(kColorPicker-Qt6)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	plasma6-xdg-desktop-portal-kde

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
%{_datadir}/gwenview
%{_datadir}/solid/actions/gwenview*.desktop
%{_datadir}/qlogging-categories6/gwenview.categories
%{_iconsdir}/*/*/*/gwenview*
%{_iconsdir}/*/*/*/document-share*
%{_qtdir}/plugins/kf6/kfileitemaction/slideshowfileitemaction.so
%{_qtdir}/plugins/kf6/parts/gvpart.so
%{_libdir}/libgwenviewlib.so*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n gwenview-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang gwenview --all-name --with-html
