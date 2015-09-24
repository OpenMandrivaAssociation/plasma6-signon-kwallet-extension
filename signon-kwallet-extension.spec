#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#

%define rel 1

Summary:        KWallet integration for Sign-on framework
Name:           signon-kwallet-extension
Version: 15.08.1
Release:        %mkrel %rel
License:        GPLv2+
Group:          System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz

URL:            https://www.kde.org/

BuildRequires:  kf5-macros

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)

BuildRequires:  pkgconfig(SignOnExtension)

BuildRequires:  kwallet-devel >= 5.0

%description
KWallet integration for Sign-on framework

#------------------------------------------------------------------------------

%define keyringkwallet_major 15
%define libkeyringkwallet %mklibname keyring-kwallet %{keyringkwallet_major}

%package -n %libkeyringkwallet
Summary: Runtime library for cantor
Group: System/Libraries

%description -n %libkeyringkwallet
Runtime library for cantor

%files -n %libkeyringkwallet
%_kf5_libdir/signon/extensions/libkeyring-kwallet.so

#------------------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kf5
%make

%install
%makeinstall_std -C build



%changelog
* Fri Sep 18 2015 neoclust <neoclust> 15.08.1-1.mga6
+ Revision: 880469
- New version 15.08.1

* Wed Aug 19 2015 neoclust <neoclust> 15.08.0-1.mga6
+ Revision: 865987
- New version 15.08.0

* Wed Aug 12 2015 neoclust <neoclust> 15.07.90-2.mga6
+ Revision: 863694
- Plasma Mass Rebuild - Rebuild for new Plasma

* Sun Aug 09 2015 neoclust <neoclust> 15.07.90-1.mga6
+ Revision: 862223
- New version 15.07.90

* Sat Jul 25 2015 neoclust <neoclust> 15.04.3-1.mga6
+ Revision: 857719
- imported package signon-kwallet-extension

