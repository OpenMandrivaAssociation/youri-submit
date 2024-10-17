Name:		youri-submit
Version:	0.10
Release:	8
Summary:	Youri submit tool
License:	GPL or Artistic
Group:		Development/Other
Source:		http://youri.zarb.or/download/%{name}-%{version}.tar.bz2
Url:		https://youri.zarb.org
BuildRequires:	perl(Youri::Utils)
BuildRequires:	perl(Youri::Package::RPM::Test)
BuildRequires:	perl(Youri::Package::RPM::Generator)
BuildRequires:	perl(Youri::Repository::Test)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl-devel
BuildArch:	    noarch

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

youri-submit is a generic package submission tool. It first runs a list of
tests on each submitted package, and if no one fails, runs a list of actions on
those packages.

%prep
%setup -q

%build
%configure2_5x
%make

%check
#%__make check

%install
%makeinstall_std

%files 
%doc ChangeLog README
%config(noreplace) %{_sysconfdir}/youri
%{_bindir}/youri-submit*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_datadir}/youri
%{_sysconfdir}/bash_completion.d/%{name}


%changelog
* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 0.10-6mdv2011.0
+ Revision: 556498
- rebuild for new perl

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.10-5mdv2010.0
+ Revision: 435373
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 0.10-4mdv2009.0
+ Revision: 262953
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 0.10-3mdv2009.0
+ Revision: 262805
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.10-1mdv2008.1
+ Revision: 141006
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Apr 25 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.0
+ Revision: 18318
- Import youri-submit



* Sun Apr 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.0
- first mdv release
