#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Params
%define		pnam	Check
Summary:	Params::Check - a generic input parsing/checking mechanism
Summary(pl.UTF-8):	Params::Check - ogólny mechanizm analizy i sprawdzania wejścia
Name:		perl-Params-Check
Version:	0.32
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	887b049db1d150cabef0fc62d51c16c2
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

%description -l pl.UTF-8
Moduł Perla Params::Check to ogólny mechanizm do analizy i sprawdzania
wejścia. Pozwala na sprawdzanie poprawności wejścia poprzez szablon.
Jedynym wymaganiem jest to, żeby argumenty były nazwane. Params::Check
może zrobić następujące rzeczy:
- przekształcić wszystkie klucze na małe litery
- sprawdzić, czy wszystkie wymagane argumenty zostały podane
- ustawić nie podane argumenty na wartości domyślne
- oddzielić argumenty nieobsługiwane i ostrzec o nich użytkownika
- sprawdzić poprawność podanych przez użytkownika argumentów w oparciu
  o łańcuchy znaków, wyrażenia regularne, listy lub nawet procedury
- wymusić spójność typów w razie potrzeby.

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
