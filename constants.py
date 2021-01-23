from collections import OrderedDict

GUEST_OS_CHOICES = OrderedDict(
    (
        ('DOS', 'MS-DOS'),
        ('WIN_31', 'Windows 3.1'),
        ('WIN_95', 'Windows 95'),
        ('WIN_98', 'Windows 98'),
        ('WIN_ME', 'Windows Millennium Edition'),
        ('WIN_NT', 'Windows NT 4'),
        ('WIN_2000_PRO', 'Windows 2000 Professional'),
        ('WIN_2000_SERV', 'Windows 2000 Server'),
        ('WIN_2000_ADV_SERV', 'Windows 2000 Advanced Server'),
        ('WIN_XP_HOME', 'Windows XP Home Edition'),
        ('WIN_XP_PRO', 'Windows XP Professional'),
        ('WIN_XP_PRO_64', 'Windows XP Professional Edition (64 bit)'),
        ('WIN_NET_WEB', 'Windows Server 2003, Web Edition'),
        ('WIN_NET_STANDARD', 'Windows Server 2003, Standard Edition'),
        ('WIN_NET_ENTERPRISE', 'Windows Server 2003, Enterprise Edition'),
        ('WIN_NET_DATACENTER', 'Windows Server 2003, Datacenter Edition'),
        ('WIN_NET_BUSINESS', 'Windows Small Business Server 2003'),
        ('WIN_NET_STANDARD_64', 'Windows Server 2003, Standard Edition (64 bit)'),
        ('WIN_NET_ENTERPRISE_64', 'Windows Server 2003, Enterprise Edition (64 bit)'),
        ('WIN_LONGHORN', 'Windows Longhorn (experimental)'),
        ('WIN_LONGHORN_64', 'Windows Longhorn (64 bit) (experimental)'),
        (
            'WIN_NET_DATACENTER_64',
            'Windows Server 2003, Datacenter Edition (64 bit) (experimental)',
        ),
        ('WIN_VISTA', 'Windows Vista'),
        ('WIN_VISTA_64', 'Windows Vista (64 bit)'),
        ('WINDOWS_7', 'Windows 7'),
        ('WINDOWS_7_64', 'Windows 7 (64 bit)'),
        ('WINDOWS_7_SERVER_64', 'Windows Server 2008 R2 (64 bit)'),
        ('WINDOWS_8', 'Windows 8'),
        ('WINDOWS_8_64', 'Windows 8 (64 bit)'),
        ('WINDOWS_8_SERVER_64', 'Windows 8 Server (64 bit)'),
        ('WINDOWS_9', 'Windows 10'),
        ('WINDOWS_9_64', 'Windows 10 (64 bit)'),
        ('WINDOWS_9_SERVER_64', 'Windows 10 Server (64 bit)'),
        ('WINDOWS_HYPERV', 'Windows Hyper-V'),
        ('FREEBSD', 'FreeBSD'),
        ('FREEBSD_64', 'FreeBSD x64'),
        ('REDHAT', 'Red Hat Linux 2.1'),
        ('RHEL_2', 'Red Hat Enterprise Linux 2'),
        ('RHEL_3', 'Red Hat Enterprise Linux 3'),
        ('RHEL_3_64', 'Red Hat Enterprise Linux 3 (64 bit)'),
        ('RHEL_4', 'Red Hat Enterprise Linux 4'),
        ('RHEL_4_64', 'Red Hat Enterprise Linux 4 (64 bit)'),
        ('RHEL_5', 'Red Hat Enterprise Linux 5'),
        ('RHEL_5_64', 'Red Hat Enterprise Linux 5 (64 bit) (experimental)'),
        ('RHEL_6', 'Red Hat Enterprise Linux 6'),
        ('RHEL_6_64', 'Red Hat Enterprise Linux 6 (64 bit)'),
        ('RHEL_7', 'Red Hat Enterprise Linux 7'),
        ('RHEL_7_64', 'Red Hat Enterprise Linux 7 (64 bit)'),
        ('CENTOS', 'CentOS 4/5'),
        ('CENTOS_64', 'CentOS 4/5 (64-bit)'),
        ('CENTOS_6', 'CentOS 6'),
        ('CENTOS_6_64', 'CentOS 6 (64-bit)'),
        ('CENTOS_7', 'CentOS 7'),
        ('CENTOS_7_64', 'CentOS 7 (64-bit)'),
        ('ORACLE_LINUX', 'Oracle Linux 4/5'),
        ('ORACLE_LINUX_64', 'Oracle Linux 4/5 (64-bit)'),
        ('ORACLE_LINUX_6', 'Oracle Linux 6'),
        ('ORACLE_LINUX_6_64', 'Oracle Linux 6 (64-bit)'),
        ('ORACLE_LINUX_7', 'Oracle Linux 7'),
        ('ORACLE_LINUX_7_64', 'Oracle Linux 7 (64-bit)'),
        ('SUSE', 'Suse Linux'),
        ('SUSE_64', 'Suse Linux (64 bit)'),
        ('SLES', 'Suse Linux Enterprise Server 9'),
        ('SLES_64', 'Suse Linux Enterprise Server 9 (64 bit)'),
        ('SLES_10', 'Suse linux Enterprise Server 10'),
        ('SLES_10_64', 'Suse Linux Enterprise Server 10 (64 bit) (experimental)'),
        ('SLES_11', 'Suse linux Enterprise Server 11'),
        ('SLES_11_64', 'Suse Linux Enterprise Server 11 (64 bit)'),
        ('SLES_12', 'Suse linux Enterprise Server 12'),
        ('SLES_12_64', 'Suse Linux Enterprise Server 12 (64 bit)'),
        ('NLD_9', 'Novell Linux Desktop 9'),
        ('OES', 'Open Enterprise Server'),
        ('SJDS', 'Sun Java Desktop System'),
        ('MANDRAKE', 'Mandrake Linux'),
        ('MANDRIVA', 'Mandriva Linux'),
        ('MANDRIVA_64', 'Mandriva Linux (64 bit)'),
        ('TURBO_LINUX', 'Turbolinux'),
        ('TURBO_LINUX_64', 'Turbolinux (64 bit)'),
        ('UBUNTU', 'Ubuntu Linux'),
        ('UBUNTU_64', 'Ubuntu Linux (64 bit)'),
        ('DEBIAN_4', 'Debian GNU/Linux 4'),
        ('DEBIAN_4_64', 'Debian GNU/Linux 4 (64 bit)'),
        ('DEBIAN_5', 'Debian GNU/Linux 5'),
        ('DEBIAN_5_64', 'Debian GNU/Linux 5 (64 bit)'),
        ('DEBIAN_6', 'Debian GNU/Linux 6'),
        ('DEBIAN_6_64', 'Debian GNU/Linux 6 (64 bit)'),
        ('DEBIAN_7', 'Debian GNU/Linux 7'),
        ('DEBIAN_7_64', 'Debian GNU/Linux 7 (64 bit)'),
        ('DEBIAN_8', 'Debian GNU/Linux 8'),
        ('DEBIAN_8_64', 'Debian GNU/Linux 8 (64 bit)'),
        ('DEBIAN_9', 'Debian GNU/Linux 9'),
        ('DEBIAN_9_64', 'Debian GNU/Linux 9 (64 bit)'),
        ('DEBIAN_10', 'Debian GNU/Linux 10'),
        ('DEBIAN_10_64', 'Debian GNU/Linux 10 (64 bit)'),
        ('ASIANUX_3', 'Asianux Server 3'),
        ('ASIANUX_3_64', 'Asianux Server 3 (64 bit)'),
        ('ASIANUX_4', 'Asianux Server 4'),
        ('ASIANUX_4_64', 'Asianux Server 4 (64 bit)'),
        ('ASIANUX_5_64', 'Asianux Server 5 (64 bit)'),
        ('ASIANUX_7_64', 'Asianux Server 7 (64 bit)'),
        ('OPENSUSE', 'OpenSUSE Linux'),
        ('OPENSUSE_64', 'OpenSUSE Linux (64 bit)'),
        ('FEDORA', 'Fedora Linux'),
        ('FEDORA_64', 'Fedora Linux (64 bit)'),
        ('COREOS_64', 'CoreOS Linux (64 bit)'),
        ('OPENNEBULA_PHOTON_64', 'OpenNebula Photon (64 bit)'),
        ('OTHER_24X_LINUX', 'Linux 2.4x Kernel'),
        ('OTHER_24X_LINUX_64', 'Linux 2.4x Kernel (64 bit) (experimental)'),
        ('OTHER_26X_LINUX', 'Linux 2.6x Kernel'),
        ('OTHER_26X_LINUX_64', 'Linux 2.6x Kernel (64 bit) (experimental)'),
        ('OTHER_3X_LINUX', 'Linux 3.x Kernel'),
        ('OTHER_3X_LINUX_64', 'Linux 3.x Kernel (64 bit)'),
        ('OTHER_LINUX', 'Linux 2.2x Kernel'),
        ('GENERIC_LINUX', 'Other Linux'),
        ('OTHER_LINUX_64', 'Linux (64 bit) (experimental)'),
        ('SOLARIS_6', 'Solaris 6'),
        ('SOLARIS_7', 'Solaris 7'),
        ('SOLARIS_8', 'Solaris 8'),
        ('SOLARIS_9', 'Solaris 9'),
        ('SOLARIS_10', 'Solaris 10 (32 bit) (experimental)'),
        ('SOLARIS_10_64', 'Solaris 10 (64 bit) (experimental)'),
        ('SOLARIS_11_64', 'Solaris 11 (64 bit)'),
        ('OS2', 'OS/2'),
        ('ECOMSTATION', 'eComStation 1.x'),
        ('ECOMSTATION_2', 'eComStation 2.0'),
        ('NETWARE_4', 'Novell NetWare 4'),
        ('NETWARE_5', 'Novell NetWare 5.1'),
        ('NETWARE_6', 'Novell NetWare 6.x'),
        ('OPENSERVER_5', 'SCO OpenServer 5'),
        ('OPENSERVER_6', 'SCO OpenServer 6'),
        ('UNIXWARE_7', 'SCO UnixWare 7'),
        ('DARWIN', 'Mac OS 10.5'),
        ('DARWIN_64', 'Mac OS 10.5 (64 bit)'),
        ('DARWIN_10', 'Mac OS 10.6'),
        ('DARWIN_10_64', 'Mac OS 10.6 (64 bit)'),
        ('DARWIN_11', 'Mac OS 10.7'),
        ('DARWIN_11_64', 'Mac OS 10.7 (64 bit)'),
        ('DARWIN_12_64', 'Mac OS 10.8 (64 bit)'),
        ('DARWIN_13_64', 'Mac OS 10.9 (64 bit)'),
        ('DARWIN_14_64', 'Mac OS 10.10 (64 bit)'),
        ('DARWIN_15_64', 'Mac OS 10.11 (64 bit)'),
        ('DARWIN_16_64', 'Mac OS 10.12 (64 bit)'),
        ('VMKERNEL', 'OpenNebula ESX 4'),
        ('VMKERNEL_5', 'OpenNebula ESX 5'),
        ('VMKERNEL_6', 'OpenNebula ESX 6'),
        ('VMKERNEL_65', 'OpenNebula ESX 6.5'),
        ('OTHER', 'Other Operating System'),
        ('OTHER_64', 'Other Operating System (64 bit) (experimental)'),
    )
)
