Summary:	Fast and easy to use image viewer for KDE
Name:		gwenview
Epoch:		2
Version:	14.12.0
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
# Drop inode/directory, add image/svg+xml and image/svg+xml-compressed
Patch0:		gwenview-4.11.0-mimetypes.patch
BuildRequires:	extra-cmake-modules5
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(libkdcraw)
BuildRequires:	pkgconfig(libkipi)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(zlib)
Requires:	kipi-common
Obsoletes:	%{name}-devel < 2:4.10.3-3
%kde5_base_reqs

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
%doc %{_docdir}/HTML/en/gwenview/
%{_bindir}/gwenview
%{_datadir}/applications/gwenview.desktop
%{_libdir}/qt5/plugins/gvpart.so
%{_datadir}/appdata/gwenview.appdata.xml
%{_datadir}/gvpart
%{_datadir}/gwenview
%{_datadir}/kservices5/gvpart.desktop
%{_datadir}/kservices5/ServiceMenus/slideshow.desktop
%{_datadir}/kxmlgui5/gwenview
%{_iconsdir}/*/*/*/gwenview*
%{_iconsdir}/*/*/*/document-share*

#------------------------------------------------

%define gwenviewlib_major 5
%define libgwenviewlib %mklibname gwenviewlib %{gwenviewlib_major}

%package -n %{libgwenviewlib}
Summary:	Gwenview library
Group:		System/Libraries
# liblcms2.so.2 is provided by LibreOffice package by mistake in Main Release
#so make sure proper liblcms2_2 package is installed in Rosa 2012.1
%if %{mdvver} == 201210
Requires:	%{_lib}lcms2_2
%endif

%description -n %{libgwenviewlib}
Gwenview library.

%files -n %{libgwenviewlib}
%{_libdir}/libgwenviewlib.so.%{gwenviewlib_major}*
%{_libdir}/libgwenviewlib.so.4.97*

#----------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%cmake_kde5

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install

# We don't need this as we don't have any devel headers
rm -f %{buildroot}%{_libdir}/libgwenviewlib.so
