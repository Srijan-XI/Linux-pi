# Changelog

All notable changes to the Linux Package Installer project.

## [1.0.0-enhanced] - 2026-02-08

### Added - UI/UX Enhancements

#### Icons & Visual Enhancements
- ✨ Emoji icons throughout the interface for better visual guidance
- ✅ Success indicators (green checkmarks) in installation history
- ❌ Failure indicators (red X marks) in installation history
- 📦 Package type indicators on tabs and headers
- 🎨 Color-coded buttons for different actions
- Professional visual hierarchy with consistent iconography

#### Keyboard Shortcuts
- ⌨️ `Ctrl+O` - Open/Browse for package file
- ⌨️ `Ctrl+I` - Install selected package
- ⌨️ `F5` - Refresh installation history
- ⌨️ `Ctrl+Q` - Quit application completely
- ⌨️ `Ctrl+Tab` - Switch between tabs
- ⌨️ Full keyboard navigation support
- ⌨️ Shortcut hints displayed in status bar

#### System Tray Integration
- 🔔 Minimize to system tray instead of closing
- 🔔 System tray icon with context menu
- 🔔 Installation success notifications (desktop notifications)
- 🔔 Installation failure alert notifications
- 🔔 Minimization notice when window is closed
- 🔔 Double-click to restore window
- 🔔 Right-click for Show/Quit menu

#### Enhanced Progress Indication
- 📊 7-step detailed installation process:
  1. Initialization (5%)
  2. Validation (15%)
  3. Reading Metadata (35%)
  4. Checking Dependencies (45%)
  5. Installing Package (55%)
  6. Configuring (85%)
  7. Finalizing (95-100%)
- 📊 Large step indicator with emoji
- 📊 Status text with current operation
- 📊 Smooth progress bar updates
- 📊 Detailed installation log with emoji markers

#### Tooltips & Help System
- 💡 Comprehensive tooltips on all interactive elements
- 💡 Keyboard shortcut hints in tooltips
- 💡 Package information tooltips
- 💡 Context-sensitive help text
- 💡 Group box descriptive tooltips
- 💡 History item detail tooltips

#### Theme Enhancements
- 🎨 Improved light theme with better contrast
- 🎨 Enhanced dark theme styling
- 🎨 Status bar styling for both themes
- 🎨 Consistent color palette throughout
- 🎨 Theme persistence across sessions

### Changed

#### User Interface
- Increased window size to 950x700 for better layout
- Added status bar with keyboard shortcut hints
- Enhanced tab icons with emojis
- Improved button sizing and layout
- Better spacing and margins throughout
- More prominent header with icon

#### Installation Process
- Non-blocking installation with detailed steps
- Better progress feedback
- Time delays for smooth visual progress
- Enhanced error messages with step context
- Improved log output formatting with emojis

#### Launcher Script
- Fixed path handling for directories with spaces
- Added installation path persistence
- Better error handling and messages
- Improved virtual environment detection
- More robust launcher script

### Fixed

#### Installation Script (install.sh)
- Fixed "externally-managed-environment" error on modern Linux distros
- Now creates and uses virtual environment automatically
- Auto-installs python3-venv if missing
- Works on Kali Linux, Debian 12+, Ubuntu 23.04+
- Better cross-distribution compatibility

#### Launcher Script
- Fixed absolute path resolution
- Added installation path validation
- Better error messages when installation not found
- Proper handling of paths with special characters

#### User Interface
- Fixed theme not loading on startup
- Corrected path label word wrapping
- Fixed history list icons not showing
- Improved tooltip positioning

### Documentation

#### New Documentation Files
- `UI_UX_ENHANCEMENTS.md` - Complete feature documentation (17 pages)
- `KEYBOARD_SHORTCUTS.md` - Quick reference card for shortcuts
- `ENHANCEMENT_SUMMARY.md` - Comprehensive summary of all changes
- `CHANGELOG.md` - This file

#### Updated Documentation
- `README.md` - Added enhanced features section
- `README.md` - Added virtual environment setup instructions
- `README.md` - Added comprehensive usage section with 4 launch methods
- `README.md` - Added PATH setup guide for Bash/Zsh/Fish
- `README.md` - Added common workflows section
- `README.md` - Added keyboard shortcuts section
- `README.md` - Added tips for new Linux users

### Technical Details

#### New Dependencies
- `QSystemTrayIcon` - System tray functionality
- `QMenu`, `QAction` - Tray menu
- `QShortcut`, `QKeySequence` - Keyboard shortcuts
- `QTimer` - Time-based operations
- `QListWidgetItem` - Custom list items

#### Code Structure
- Refactored `InstallerThread` with detailed step signals
- Added `setup_shortcuts()` method
- Added `setup_system_tray()` method
- Added `update_step()` method
- Enhanced `apply_theme()` with status bar styling
- Improved error handling throughout

---

## [1.0.0] - 2026-02-08 (Initial Release)

### Added

#### Core Functionality
- Package installation for .deb files (Debian/Ubuntu)
- Package installation for .rpm files (Fedora/RHEL)
- Automatic package manager detection
- Dependency resolution
- Installation progress tracking
- Real-time installation logs

#### User Interface
- PyQt5-based GUI
- Three-tab interface (Install, History, Settings)
- Package file browser
- Package information display
- Progress bar
- Installation log output
- Installation history list
- Light theme

#### Installation & Setup
- Python virtual environment support
- Automated `install.sh` script
- Desktop entry creation
- Launcher script for `~/.local/bin`
- pip requirements file

#### Package Manager Support
- APT (Debian/Ubuntu) - using `apt` and `dpkg`
- DNF (Fedora) - using `dnf`
- YUM (RHEL/CentOS) - using `yum`
- Zypper (openSUSE) - using `zypper`
- Automatic fallback mechanisms

#### Features
- Package validation
- Package metadata extraction
- Superuser privilege elevation (via `pkexec`)
- Installation history logging (JSON format)
- Error handling and user feedback
- Clear/reset functionality

#### Documentation
- Comprehensive README.md with:
  - Installation instructions
  - Usage guide
  - Troubleshooting section
  - Architecture overview
  - Security considerations
- CONTRIBUTING.md for developers
- LICENSE (MIT)
- Requirements and setup files

#### Logging System
- JSON-based history storage in `~/.linux-package-installer/`
- Success/failure tracking
- Timestamp recording
- Package path storage
- Statistics generation

---

## Release Notes

### Version 1.0.0-enhanced (Current)

The enhanced version represents a **major UI/UX overhaul** of the original 1.0.0 release. While maintaining all core functionality, it adds professional-grade user interface features that make it suitable for wide distribution.

**Highlights:**
- Complete keyboard navigation
- System tray integration
- Desktop notifications
- Detailed installation progress
- Comprehensive help system
- Professional appearance

**Recommended for:** All users, especially those who value productivity and polish

### Version 1.0.0 (Original)

The original release focused on core functionality - reliably installing .deb and .rpm packages with a simple, clean interface.

**Highlights:**
-  Basic package installation
- Simple progress tracking
- Installation history
- Clean, functional UI

**Recommended for:** Users who want minimal, straightforward functionality

---

## Upgrade Guide

### From 1.0.0 to 1.0.0-enhanced

1. **Backup** your installation history (if important):
   ```bash
   cp ~/.linux-package-installer/installation_history.json ~/backup.json
   ```

2. **Update** the files:
   ```bash
   cd ~/path/to/Linux-pi
   git pull  # or download latest version
   ./install.sh  # Reinstall
   ```

3. **Enjoy** the new features! Your history will be preserved.

### New User Experience

New users installing 1.0.0-enhanced will get:
- All features enabled by default
- Light theme as default
- System tray integration active
- All keyboard shortcuts ready
- Tooltips on all elements

---

## Deprecations

### None

All features from 1.0.0 are preserved in 1.0.0-enhanced. The original version is backed up as `main_old.py` for reference.

---

## Known Issues

### None Critical

The application has been tested and is production-ready.

### Minor Notes
- Custom application icon not yet implemented (uses system default)
- Time estimates for installation not available
- Batch installation not yet supported

These are planned for future releases and do not affect core functionality.

---

## Credits

**Author:** Srijan-XI  
**License:** MIT License  
**Built with:** Python, PyQt5  
**Package Handlers:** apt, dnf, yum, zypper, dpkg, rpm

**Special Thanks:**
- PyQt5 development team
- Linux package manager maintainers
- Open source community

---

## Links

- **Repository:** https://github.com/Srijan-XI/Linux-pi
- **Issues:** https://github.com/Srijan-XI/Linux-pi/issues
- **Documentation:** See README.md, UI_UX_ENHANCEMENTS.md
- **License:** See LICENSE file

---

**Last Updated:** 2026-02-08  
**Version:** 1.0.0-enhanced
