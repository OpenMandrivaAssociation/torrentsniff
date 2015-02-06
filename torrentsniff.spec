%define name torrentsniff
%define version 0.3.0
%define release 11
#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

Summary: Reports status information of BitTorrent distributed downloads
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.highprogrammer.com/alan/perl/%{name}-%{version}.tar.bz2
License: MIT
Group: Networking/File transfer
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://www.highprogrammer.com/alan/perl/torrentsniff.html
BuildArch: noarch

%description
TorrentSniff reports status information for a given torrent including the
current number of complete copies (seeds) and incomplete copies (leeches)
currently active.  TorrentSniff is derived from TorrentSpy 0.1.0.3-BETA.


%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_bindir %buildroot%perl_vendorlib
install -m 755 torrentsniff %buildroot%_bindir
install -d -m 755 %buildroot%perl_vendorlib/BitTorrent
install -m 644 BitTorrent/* %buildroot%perl_vendorlib/BitTorrent

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%_bindir/torrentsniff
%perl_vendorlib/BitTorrent


%changelog
* Fri Aug 05 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.0-10mdv2012.0
+ Revision: 693276
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.3.0-9mdv2011.0
+ Revision: 261625
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.3.0-8mdv2009.0
+ Revision: 254690
- rebuild

* Thu Mar 13 2008 Andreas Hasenack <andreas@mandriva.com> 0.3.0-6mdv2008.1
+ Revision: 187630
- rebuild for 2008.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.0-5mdv2008.0
+ Revision: 57473
- Import torrentsniff



* Mon Jul 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.0-1mdv2007.0
- Rebuild

* Wed May 24 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.3.0-4mdk
- Rebuild

* Mon May 23 2005 Götz Waschk <waschk@mandriva.org> 0.3.0-3mdk
- mkrel

* Fri May 13 2005 Götz Waschk <waschk@mandriva.org> 0.3.0-2mdk
- rebuild

* Fri Apr 16 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.0-1mdk
- new version

* Sun Jun 15 2003 Götz Waschk <waschk@linux-mandrake.com> 0.2.0-1mdk
- the executable was renamed
- new version

* Mon Jun  2 2003 Götz Waschk <waschk@linux-mandrake.com> 0.1-1mdk
- initial package
