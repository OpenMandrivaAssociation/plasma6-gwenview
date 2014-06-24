Summary:	Fast and easy to use image viewer for KDE
Name:		gwenview
Epoch:		2
Version:	4.13.2
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
# Drop inode/directory, add image/svg+xml and image/svg+xml-compressed
Patch0:		gwenview-4.11.0-mimetypes.patch
BuildRequires:	kdebase4-devel
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
# liblcms2.so.2 is provided by LibreOffice package by mistake in Main Release
#so make sure proper liblcms2_2 package is installed in Rosa 2012.1
%if %{mdvver} == 201210
Requires:	%{_lib}lcms2_2
%endif

%description -n %{libgwenviewlib}
Gwenview library.

%files -n %{libgwenviewlib}
%{_kde_libdir}/libgwenviewlib.so.%{gwenviewlib_major}*

#----------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# We don't need this as we don't have any devel headers
rm -f %{buildroot}%{_kde_libdir}/libgwenviewlib.so

%changelog
* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.13.2-1
- New version 4.13.2
- Add pkgconfig(libkdcraw) to BuildRequires

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-1
- New version 4.11.0
- Re-diff mimetypes patch

* Fri Jul 19 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.5-2
- Update BuildRequires

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-1
- New version 4.10.4
- Drop no longer needed fix-rotate patch

* Mon May 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-3
- Drop devel package because it's useless here and was just wrong
- Minor spec cleanup
- Add explicit Requires on liblcms2_2 for Rosa 2012.1 backport

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-1
- New version 4.10.3

* Mon May 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-4
- Add patch to fix image rotation which was broken in 4.10

* Mon Apr 22 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-3
- Update supported mimetypes (add image/svg+xml-compressed)

* Sun Apr 21 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-2
- Update supported mimetypes (add image/svg+xml)

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.1-1
- New version 4.10.1
- Re-diff patch for desktop file

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.0-1
- New version 4.10.0
- Add pkgconfig(lcms2) and pkgconfig(libkactivities) to BuildRequires
- Re-diff patch for desktop file

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0-1
- New version 4.9.0

* Thu Jul 19 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-1
- New version 4.8.97

* Mon Jul 02 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.4-1
- update to 4.8.4

* Fri May 25 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.3-2
- drop inode/directory from desktop file

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 2:4.8.0-1
+ Revision: 762444
- New upstream tarball

* Fri Jan 06 2012 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 2:4.7.97-1
+ Revision: 758035
- New upstream tarball

* Thu Dec 22 2011 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 2:4.7.95-1
+ Revision: 744511
- New upstream tarball

* Fri Dec 09 2011 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 2:4.7.90-1
+ Revision: 739347
- New upstream tarball

* Sat Nov 19 2011 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 2:4.7.80-1
+ Revision: 731855
- New upstream tarball 4.7.80

* Tue Oct 11 2011 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 2:4.7.41-1
+ Revision: 704176
- Import gwenview
- Create current folder


* Sun Mar 04 2007 Angelo Naselli <anaselli@mandriva.org> 1.4.1-5mdv2007.0
+ Revision: 132341
- rebuilt for new libexiv2

* Mon Jan 22 2007 Angelo Naselli <anaselli@mandriva.org> 1.4.1-4mdv2007.1
+ Revision: 112122
- added patch to partially fix bko 129948

* Wed Jan 10 2007 Angelo Naselli <anaselli@mandriva.org> 1.4.1-3mdv2007.1
+ Revision: 107262
- bko 111641
- bko 131162, 132556
- bko 138467
- removed useless dependency

* Mon Dec 04 2006 Angelo Naselli <anaselli@mandriva.org> 1.4.1-2mdv2007.1
+ Revision: 90482
- rebuilt for new libexiv

* Mon Nov 27 2006 Angelo Naselli <anaselli@mandriva.org> 1.4.1-1mdv2007.1
+ Revision: 87568
- added libkexiv requirement
- New versin 1.4.1
- Import gwenview

* Tue Sep 19 2006 Angelo Naselli <anaselli@mandriva.org> 1.4.0-2mdv2007.0
- rebuilt (wrong tarball from sourceforge)

* Mon Sep 18 2006 Angelo Naselli <anaselli@mandriva.org> 1.4.0-1mdv2007.0
- New version 1.4.0

* Sun Sep 03 2006 Angelo Naselli <anaselli@mandriva.org> 1.3.93-3mdv2007.0
- Really fixed  Bug #24921

* Sat Sep 02 2006 Angelo Naselli <anaselli@mandriva.org> 1.3.93-2mdv2007.0
- Fix Bug #24921 with 1.3.1 translations, some are better the none :)

* Sun Aug 27 2006 Angelo Naselli <anaselli@mandriva.org> 1.3.93-1mdv2007.0
- New release 1.3.93

* Sun Jul 16 2006 Angelo Naselli <anaselli@mandriva.org> 1.3.92b-1mdv2007.0
- New release 1.3.92b

* Sat Jul 15 2006 Angelo Naselli <anaselli@mandriva.org> 1.3.92-1mdv2007.0
- New release 1.3.92

* Mon Jul 03 2006 Angelo Naselli <anaselli@mandriva.org> 1.3.91-2mdv2007.0
- removed -I optiion added for exif bug

* Sun Jun 25 2006 Angelo Naselli <anaselli@mandriva.org> 1.3.91-1mdv2007.0
- New release 1.3.91

* Fri Jan 13 2006 Angelo Naselli <anaselli@mandriva.org> 1.3.1-2mdk
- Rebuilt to allow building on x86_64

* Sun Nov 20 2005 Angelo Naselli <anaselli@mandriva.org> 1.3.1-1mdk
- New release 1.3.1

* Tue Sep 13 2005 Angelo Naselli <anaselli@mandriva.org> 1.3.0-1mdk
- New release 1.3.0

* Mon Aug 22 2005 Angelo Naselli <anaselli@mandriva.org> 1.2.92-1mdk
- New release 1.2.92

* Thu Jul 21 2005 Angelo Naselli <anaselli@mandriva.org> 1.2.91-1mdk
- New release 1.2.91
- patched for fvisibility problem (aligned to svn)

* Tue May 10 2005 Laurent MONTEL <lmontel@mandriva.com> 1.2.0-4
- Real fix build on x86_64

* Mon May 09 2005 Angelo Naselli <anaselli@mandriva.org> 1.2.0-3mdk
- fix for x86_64 arch

* Mon May 09 2005 Angelo Naselli <anaselli@mandriva.org> 1.2.0-2mdk
- Rebuild

* Mon Apr 04 2005 Angelo Naselli <anaselli@mandrake.org> 1.2.0-1mdk
- really built new version

* Sun Mar 20 2005 Angelo Naselli <anaselli@mandrake.org> 1.2.0-0.pre4.2mdk
- really built new version

* Sun Mar 20 2005 Angelo Naselli <anaselli@mandrake.org> 1.2.0-0.pre4.1mdk
- new version

* Sat Mar 19 2005 Angelo Naselli <anaselli@mandrake.org> 1.2.0-0.pre3.2mdk
- fix bug #14731

* Sun Feb 27 2005 Angelo Naselli <anaselli@mandrake.org> 1.2.0-0.pre3.1mdk
- new version

* Sun Feb 13 2005 Angelo Naselli <anaselli@mandrake.org> 1.2.0-0.pre2.2mdk
- define mkrel macro if not exist

* Sun Feb 13 2005 Angelo Naselli <anaselli@mandrake.org> 1.2.0-0.pre2.1mdk
- new version

* Sat Jan 29 2005 Angelo Naselli <anaselli@mandrake.org> 1.2.0-0.pre1.2mdk
- added patch to make it compile for mdk official 10.1
- added patch to fix zoom (from cvs)
- added patch to add missing files (from cvs)

* Mon Jan 24 2005 Angelo Naselli <anaselli@mandrake.org> 1.2.0-0.pre1.1mdk
- new version

* Wed Jan 19 2005 Angelo Naselli <anaselli@mandrake.org> 1.1.8-0.4mdk
- fix bug 13100

* Sun Jan 16 2005 Angelo Naselli <anaselli@mandrake.org> 1.1.8-0.3mdk
- better handling of symlink

* Thu Jan 13 2005 Angelo Naselli <anaselli@mandrake.org> 1.1.8-0.2mdk
- fix double click into kpart

* Sun Jan 09 2005 Angelo Naselli <anaselli@mandrake.org> 1.1.8-0.1mdk
- 1.1.8 
- fix Requires section to be compliant to the library policy

* Thu Dec 30 2004 Angelo Naselli <anaselli@mandrake.org> 1.1.7-0.5mdk
- added 1.1.7b patch (solved some build problems)

* Wed Dec 29 2004 Angelo Naselli <anaselli@mandrake.org> 1.1.7-0.4mdk
- description restyling

* Sun Dec 26 2004 Angelo Naselli <anaselli@mandrake.org> 1.1.7-0.3mdk
- fix Require and Provide section

* Sun Dec 26 2004 Angelo Naselli <anaselli@mandrake.org> 1.1.7-0.2mdk
- removed hack management
- added distro-specific release tag management 
  use option "--with official" to build mdk official package

* Mon Dec 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.7-0.1mdk
- 1.1.7

* Fri Dec 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.6-0.2mdk
- Fix spec file

* Mon Oct 25 2004 Angelo Naselli <anaselli@mandrake.org> 1.1.6-0.1mdk
- new version
  *  New features:
   o The application now has two modes: browse and view. Browse mode shows 
     all views: folder, file and image. View mode only shows the image. 
     Gwenview starts in browse mode except if an image URL is given as 
     an argument. You can switch between modes using the toolbar button, 
     or with the "View/Browse mode" menu item or with the Ctrl+Return shortcut.
   o JPEGTran code has been integrated into Gwenview, there's no need to install 
     it separately anymore.
  * Fixes:
   o Update the EXIF thumbnail when rotating a JPEG file.
   o In the folder view, folders now open with a single click (By Daniel Thaler).
   o Reworked coordinate conversions in order to avoid subtle paint errors.
   o Remember computed optimal repaint sizes in the config file, 
     so they are available immediately after next start.
   o Remember shown URL after session restore.

* Sun Oct 17 2004 Angelo Naselli <anaselli@mandrake.org> 1.1.5-0.3mdk
- rebuilt for new liblipi + fixing

* Sun Oct 10 2004 Angelo Naselli <anaselli@mandrake.org> 1.1.5-0.2mdk
- applied Lubos Lunak's patch to avoid printing crash using Konqueror

* Tue Sep 21 2004 Angelo Naselli <anaselli@mandrake.org> 1.1.5-0.1mdk
- new version
   *  New features:
    o The thumbnail progress bar and stop buttons are now embedded in the thumbnail view.
    o The location bar now shows the file names instead of the folders.
    o The thumbnails toolbar buttons have been moved to a specialized file view toolbar.
    o It's now possible to assign key shortcuts to KIPI plugins.
    o New manpage by Christopher Martin.
   * Fixes:
    o Do not display the folder name as an image in the status bar.
    o Make sure the folder KPart starts in the right folder.
    o Unbreak the saving of key shortcuts.
    o Remote urls are correctly bookmarked.
    o Do not try to overwrite the trash when trashing only one file.

* Mon Aug 30 2004 Angelo Naselli <random_lx@yahoo.com> 1.1.4-0.2mdk
- patch for russian language

* Wed Aug 25 2004 Angelo Naselli <anaselli@mandrake.org> 1.1.4-0.1mdk
- changed spec file to manage -with-hack option to build gwenview with 
  hack suffix (default is without hack)
- from Aurélien Gâteau:
- New features:
 - In the thumbnail view, It's now possible to sort images in reverse order.
 - Use EXIF-stored thumbnail if available.
 - Option to disable saving of generated thumbnails to cache.
 - In fullscreen mode, it's now possible to display the image comment or size
   in addition to the file path.
 - The fullscreen On-Screen-Display is more readable now.
 - The background color of the image view can be configured.
 - When printing, it's now possible to enlarge images so that they fill the
   page.
- Fixes:
 - In the folder view, pressing Enter now opens the selected folder.
 - Use icon list for the configuration dialog.
 - Avoid data loss if the JPEG images are saved while being rotated by
   JPEGTran.
 - The back button in Konqueror now works correctly with gvimagepart.
 - The default layout is more user-friendly.
 - Non-trivial URLs (e.g. http query URL) are correctly handled.
 - You can now drop images on the image view.

* Sun Jun 13 2004 Angelo Naselli <random_lx@yahoo.com> 1.1.3-0.1mdk
- new release: my wedding present :-)
   from Aurélien Gâteau:
   Gwenview codenamed "Hurry up, I'm getting married tomorrow"
   *  New features:
          o You can now define custom branches in the dir view (By Craig Drummond)
          o An image cache has been added to speedup image loading.
          o Gwenview now uses freedesktop.org thumbnail spec to store thumbnails.
          o A new option to automatically empty thumbnail cache on exit (By Angelo Naselli).
          o The image size is now displayed below file names in thumbnail view.
    * Fixes:
          o Don't crash when switching to fullscreen while generating thumbnails and coming back (By Lubos Lunak)
          o Faster thumbnail generation (By Lubos Lunak)
          o Faster image painting by dynamically determining suitable paint size (By Lubos Lunak)
          o Use the "Standard Background" color as the background for thumbnails and folders (By Craig Drummond).
          o Make sure the current image is reloaded if it has been modified outside Gwenview.

* Wed Jun 02 2004 Angelo Naselli <random_lx@yahoo.com> 1.1.2-0.3mdk
- hack suffix on kpart lib

* Fri May 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.1.2-0.2mdk
- merge with changes from Angelo Naselli <random_lx@yahoo.com>

* Thu May 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.1.2-0.1mdk
- 1.1.2
- from Angelo Naselli <random_lx@yahoo.com> : 
- mdk version of the development release (1.1.1) named gwenview_hack
    from Aurélien Gâteau:
    - New features:
     - Added KPart support, this installs in Konqueror a new file view mode and let you view 
       images in an embedded Gwenview (By Jonathan Riddell).
     - Asynchronous JPEG loading, based on Khtml loader.
     - Really asynchronous PNG loading (By Lubos Lunak).
     - Mouse wheel will now scroll the image by default. Holding Ctrl will scroll horizontally. 
       An option has been added to the setting dialog to toggle between scroll and browse 
       (By Jeroen Peters).
     - When holding shift over the image, right click will zoom out (By Jeroen Peters).
     - Image painting is now progressive (By Lubos Lunak).
    - Fixes:
     - The rotate and mirror functions can now work on multiple selection.
     - Make it possible to load another image or quit even if you can't save your changes.
     - Gwenview won't spawn multiple instances of jpegtran anymore.

