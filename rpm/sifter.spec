# Generated from src/lib/rpmSpec.ts — do not hand-edit.
#
# Build on COPR with "Upload a spec file": COPR resolves Source0 over the
# network when it builds the SRPM, so nothing has to be uploaded alongside.

%global debug_package %{nil}
%global __os_install_post %{nil}

Name:           sifter
Version:        0.3.137
Release:        1%{?dist}
Summary:        One library and one Play button for every game you own.
License:        LicenseRef-Proprietary
URL:            https://www.siftergames.com
Source0:        https://www.siftergames.com/dl/0.3.137/Sifter-linux.deb#/sifter-%{version}.deb
ExclusiveArch:  x86_64

BuildRequires:  binutils
BuildRequires:  tar
Requires:       webkit2gtk4.1
Requires:       gtk3
Requires:       libappindicator-gtk3
Requires:       hicolor-icon-theme

%description
Sifter puts every game you own in one library and launches any of it from one place.
It finds what is installed on your PC across Steam, Epic, GOG, Xbox, EA, Ubisoft,
Battle.net, Amazon and itch.io, and signing in to Steam, Xbox, Epic, GOG, itch.io or
Amazon brings in the games you own but have not installed.
Free, with no ads and nothing sold.

%prep
ar x %{SOURCE0}
tar xf data.tar*

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 usr/bin/sifter-desktop %{buildroot}%{_bindir}/sifter-desktop
mkdir -p %{buildroot}%{_datadir}
cp -r usr/share/applications %{buildroot}%{_datadir}/
cp -r usr/share/icons %{buildroot}%{_datadir}/

%files
%{_bindir}/sifter-desktop
%{_datadir}/applications/Sifter.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/sifter-desktop.png

%changelog
* Mon Jan 01 2024 Sifter Games <hello@siftergames.com> - 0.3.137-1
- Automated build. See https://www.siftergames.com/changelog
