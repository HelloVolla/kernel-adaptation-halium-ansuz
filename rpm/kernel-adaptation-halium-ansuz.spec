# Device details
%define device halium-ansuz

# Kernel target architecture
%define kernel_arch arm64

%define kcflags "KCFLAGS="

#Compiler to use
%define makeopts LLVM=1 LLVM_IAS=1
%define clangtriple aarch64-linux-gnu-
%define crosscompile aarch64-linux-gnu-
%define crosscompile32 arm-linux-androideabi-
%define hostldflags "-fuse-ld=lld --rtlib=compiler-rt"

# RPM target architecture, remove to leave it unaffected
# You should have a good reason to change the target architecture
# (like building on aarch64 targeting an armv7hl repository)
%define device_target_cpu aarch64

# Defconfig to pick-up
%define defconfig gki_defconfig halium.config
%define extra_config sfos-ansuz.config
%define kernel_config %{defconfig} %{extra_config}

# Linux kernel source directory
%define source_directory linux

# Build modules
%define build_modules 1

# Build Image
%define build_Image 1

# Apply Patches
%define apply_patches 1

%define build_vendor_boot 1

# Build and pick-up the following devicetrees
##define devicetrees

#Device Info
%define deviceinfo_kernel_cmdline bootopt=64S3,32N2,64N2 systempart=/dev/mapper/system
%define deviceinfo_bootimg_prebuilt_dtb volla-ansuz.dtb
%define deviceinfo_ramdisk_compression lz4
%define deviceinfo_flash_pagesize 4096
%define deviceinfo_flash_offset_base 0x0
%define deviceinfo_flash_offset_kernel 0x40000000
%define deviceinfo_flash_offset_ramdisk 0x66f00000
%define deviceinfo_flash_offset_tags 0x47c80000
%define deviceinfo_flash_offset_dtb 0x47c80000
%define deviceinfo_bootimg_qcdt false
%define deviceinfo_bootimg_header_version 4
%define deviceinfo_bootimg_has_init_boot_partition true
%define deviceinfo_bootimg_partition_size 67108864
%define deviceinfo_bootimg_os_version 14
%define deviceinfo_bootimg_os_patch_level 2025-04
%define deviceinfo_rootfs_image_sector_size 4096
%define deviceinfo_halium_version 14
%define deviceinfo_kernel_disable_modules false

Version:        6.1.145
Release:        1

%include kernel-adaptation-simplified/kernel-adaptation-simplified.inc
