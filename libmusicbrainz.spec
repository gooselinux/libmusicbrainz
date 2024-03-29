
Summary: Library for accessing MusicBrainz servers
Name: libmusicbrainz
Version: 2.1.5
Release: 11.1%{?dist}
License: LGPLv2+
Group: System Environment/Libraries
URL: http://www.musicbrainz.org/
Source0: ftp://ftp.musicbrainz.org/pub/musicbrainz/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch1: libmusicbrainz-2.1.5-gcc43.patch

BuildRequires: expat-devel

# prepare for libmusicbrainz3
Provides: libmusicbrainz2 = %{version}-%{release}

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package devel
Summary: Headers for developing programs that will use %{name} 
Group: Development/Libraries
Provides: libmusicbrainz2-devel = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}. 


%prep
%setup -q

%patch1 -p1 -b .gcc43

%{__cp} -a examples/README examples/README.examples

%build
%configure --disable-static
make %{?_smp_mflags}


%install
%{__rm} -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/lib*.la


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%doc docs/mb_howto.txt examples/README.examples examples/*.c examples/*.cpp
%{_includedir}/musicbrainz/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.1.5-11.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Bastien Nocera <bnocera@redhat.com> 2.1.5-10
- Fix ordering of the files members

* Wed Jun 10 2009 Bastien Nocera <bnocera@redhat.com> 2.1.5-9
- Update with comments from merge review (#226034)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jun 15 2008 Rex Dieter <rdieter@fedoraproject.org> 2.1.5-7
- Provides: libmusicbrainz2(-devel), prepare for libmusicbrainz3

* Fri Feb 22 2008 Rex Dieter <rdieter@fedoraproject.org> 2.1.5-6
- gcc43 patch (#434127)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.5-5
- Autorebuild for GCC 4.3

* Mon Feb 18 2008 Rex Dieter <rdieter@fedoraproject.org> - 2.1.5-4
- specfile cosmetics

* Thu Nov 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 2.1.5-3
- use versioned Obsoletes
- drop (Build)Requires: libstdc++-devel
- License: LGPLv2+

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 2.1.5-2
- Rebuild for PPC toolchain bug

* Thu Jun 21 2007 - Bastien Nocera <bnocera@redhat.com> - 2.1.5-1
- Update to 2.1.5

* Mon Oct 23 2006 Matthias Clasen <mclasen@redhat.com> - 2.1.4-1
- Update to 2.1.4

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.1.1-4.1
- rebuild

* Wed Jun  7 2006 Jeremy Katz <katzj@redhat.com> - 2.1.1-4
- rebuild for -devel deps

* Tue Apr 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.1.1-3
- apply .spec file cleanups from Matthias Saou (#172926)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.1.1-2.1
- bump again for double-long bug on ppc(64)

* Tue Feb  7 2006 Christopher Aillon <caillon@redhat.com> - 2.1.1-2
- Stop shipping the .a file in the main package

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.1.1-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 23 2005 John (J5) Palmieri <johnp@redhat.com> 2.1.1-1
- Update to upstream version 2.1.1
- Removed libmusicbrainz-2.0.2-missing-return.patch
- Removed libmusicbrainz-2.0.2-conf.patch

* Wed Mar 03 2005 John (J5) Palmieri <johnp@redhat.com> 2.0.2-14
- Add patch to fix percision cast error to compile correctly on s390x
 
* Wed Mar 03 2005 John (J5) Palmieri <johnp@redhat.com> 2.0.2-13
- rebuild with gcc 4.0

* Mon Nov 08 2004 Colin Walters <walters@redhat.com> 2.0.2-12
- Add libmusicbrainz-2.0.2-missing-return.patch (bug #137289)

* Thu Oct 07 2004 Colin Walters <walters@redhat.com> 2.0.2-11
- BuildRequire expat-devel

* Tue Sep 28 2004 Colin Walters <walters@redhat.com> 2.0.2-10
- Move .so symlink to -devel package

* Tue Aug 31 2004 Colin Walters <walters@redhat.com> 2.0.2-9
- Add ldconfig calls (bz #131281)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Dec 18 2003 Brent Fox <bfox@redhat.com> 2.0.2-6
- add a BuildPreReq for libstdc++-devel and gcc-c++ (bug #106556)
- add a Requires for libstdc++-devel for libmusicbrainz-devel

* Mon Sep  1 2003 Bill Nottingham <notting@redhat.com>
- Obsoletes musicbrainz-devel too

* Mon Sep  1 2003 Jonathan Blandford <jrb@redhat.com>
- Obsoletes musicbrainz

* Fri Aug 22 2003 Bill Nottingham <notting@redhat.com> 2.0.2-5
- fix autoconf/libtool weirdness, remove exclusivearch

* Fri Aug 22 2003 Brent Fox <bfox@redhat.com> 2.0.2-4
- add ExcludeArch for s390x (something is really broken)

* Fri Aug 22 2003 Brent Fox <bfox@redhat.com> 2.0.2-3
- add ExcludeArch for ppc64

* Fri Aug 22 2003 Brent Fox <bfox@redhat.com> 2.0.2-2
- add ExcludeArch for x86_64 for now

* Thu Aug 21 2003 Brent Fox <bfox@redhat.com> 
- Initial build.


