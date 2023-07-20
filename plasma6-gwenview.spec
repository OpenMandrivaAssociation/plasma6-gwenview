%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define git 20230720

Summary:	Fast and easy to use image viewer for KDE
Name:		gwenview
Version:	23.07.90
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%if 0%{?git}
Source0:	https://invent.kde.org/graphics/gwenview/-/archive/master/gwenview-master.tar.bz2#/gwenview-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(KF6Baloo)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Activities)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(kImageAnnotator)
BuildRequires:	cmake(WaylandProtocols)
BuildRequires:	pkgconfig(wayland-protocols)
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
%{_datadir}/kconf_update/gwenview.upd
%{_datadir}/kconf_update/gwenview-imageview-alphabackgroundmode-update.pl
%{_datadir}/gwenview
%{_datadir}/solid/actions/gwenview*.desktop
%{_datadir}/qlogging-categories6/gwenview.categories
%{_iconsdir}/*/*/*/gwenview*
%{_iconsdir}/*/*/*/document-share*
%{_qtdir}/plugins/kf6/kfileitemaction/slideshowfileitemaction.so
%{_qtdir}/plugins/kf6/parts/gvpart.so

#------------------------------------------------

%define gwenviewlib_major 5
%define libgwenviewlib %mklibname gwenviewlib %{gwenviewlib_major}

%package -n %{libgwenviewlib}
Summary:	Gwenview library
Group:		System/Libraries
Obsoletes:	%{mklibname gwenviewlib 5} < 2:19.04.0-3

%description -n %{libgwenviewlib}
Gwenview library.

%files -n %{libgwenviewlib}
%{_libdir}/libgwenviewlib.so.%{gwenviewlib_major}*
%{_libdir}/libgwenviewlib.so.4.97*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n gwenview-%{?git:master}%{!?git:%{version}}
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

# We don't need this as we don't have any devel headers
rm -f %{buildroot}%{_libdir}/libgwenviewlib.so

%find_lang gwenview --all-name --with-html
