

OS > WINDOWS: USING DUAL-BOOT WITH A LINUX DISTRO

    If applicable, in case you are using Dual-boot with some Linux distro, set Windows to use UTC time, equal to Ubuntu, for compatibility with Dual-boot. Linux works better with UTC instead of Local Time.

        >> On Windows 10 or 11 > Win+R > regedit > HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation\
                    
        >> Right-click on the right panel → New → DWORD (32-bit);

        >> Value Name it: RealTimeIsUniversal;

        >> Edit value to 1 and Decimal.
