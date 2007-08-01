%define name torrentsniff
%define version 0.3.0
%define release %mkrel 5
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
