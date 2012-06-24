#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Params
%define		pnam	Check
Summary:	Params::Check - a generic input parsing/checking mechanism
Summary(pl):	Params::Check - og�lny mechanizm analizy i sprawdzania wej�cia
Name:		perl-Params-Check
Version:	0.25
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1756a2b387544fea13b442f3be8a39dc
URL:		http://search.cpan.org/dist/Params-Check/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
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

%description -l pl
Modu� Perla Params::Check to og�lny mechanizm do analizy i sprawdzania
wej�cia. Pozwala na sprawdzanie poprawno�ci wej�cia poprzez szablon.
Jedynym wymaganiem jest to, �eby argumenty by�y nazwane. Params::Check
mo�e zrobi� nast�puj�ce rzeczy:
- przekszta�ci� wszystkie klucze na ma�e litery
- sprawdzi�, czy wszystkie wymagane argumenty zosta�y podane
- ustawi� nie podane argumenty na warto�ci domy�lne
- oddzieli� argumenty nieobs�ugiwane i ostrzec o nich u�ytkownika
- sprawdzi� poprawno�� podanych przez u�ytkownika argument�w w oparciu
  o �a�cuchy znak�w, wyra�enia regularne, listy lub nawet procedury
- wymusi� sp�jno�� typ�w w razie potrzeby.

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
%dir %{perl_vendorlib}/Params
%{perl_vendorlib}/Params/Check.pm
%{_mandir}/man3/*
