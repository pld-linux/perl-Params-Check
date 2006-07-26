#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Params
%define		pnam	Check
Summary:	perl(Params::Check)
Name:		perl-Params-Check
Version:	0.25
Release:	0.1
# note if it is "same as perl"
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1756a2b387544fea13b442f3be8a39dc
URL:		http://search.cpan.org/dist/Params-Check
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} && %{with tests}
BuildRequires:	perl-Locale-Maketext-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module Params::Check is a generic input parsing/checking
mechanism. It allows you to validate input via a template. The only
requirement is that the arguments must be named. Params::Check can do
the following things for you:
- Convert all keys to lowercase
- Check if all required arguments have been provided
- Set arguments that have not been provided to the default
- Weed out arguments that are not supported and warn about them to the
  user
- Validate the arguments given by the user based on strings, regexes,
  lists or even subroutines
- Enforce type integrity if required

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%dir %attr(755,root,root) %{perl_vendorlib}/Params
%{perl_vendorlib}/Params/Check.pm
%{_mandir}/man3/*
