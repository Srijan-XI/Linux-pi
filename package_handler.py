"""
Package Handler Module
Handles package validation, installation, and information extraction
for .deb and .rpm packages
"""

import os
import subprocess
import platform


class PackageHandler:
    """Handle package operations for .deb and .rpm files"""
    
    def __init__(self):
        self.supported_formats = ['.deb', '.rpm']
        self.package_manager = self.detect_package_manager()
    
    def detect_package_manager(self):
        """Detect the system's package manager"""
        # Check for APT (Debian/Ubuntu)
        if self._command_exists('apt'):
            return 'apt'
        elif self._command_exists('apt-get'):
            return 'apt'
        # Check for DNF (Fedora)
        elif self._command_exists('dnf'):
            return 'dnf'
        # Check for YUM (RHEL/CentOS)
        elif self._command_exists('yum'):
            return 'yum'
        # Check for Zypper (openSUSE)
        elif self._command_exists('zypper'):
            return 'zypper'
        else:
            return 'unknown'
    
    def _command_exists(self, command):
        """Check if a command exists on the system"""
        try:
            subprocess.run(
                ['which', command],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def validate_package(self, package_path):
        """Validate if the package file is supported and exists"""
        if not os.path.exists(package_path):
            return False
        
        _, ext = os.path.splitext(package_path)
        return ext.lower() in self.supported_formats
    
    def get_package_type(self, package_path):
        """Get the package type (.deb or .rpm)"""
        _, ext = os.path.splitext(package_path)
        return ext.lower()
    
    def get_package_info(self, package_path):
        """Extract package information"""
        package_type = self.get_package_type(package_path)
        
        try:
            if package_type == '.deb':
                return self._get_deb_info(package_path)
            elif package_type == '.rpm':
                return self._get_rpm_info(package_path)
            else:
                return "Unsupported package format"
        except Exception as e:
            return f"Error reading package info: {str(e)}"
    
    def _get_deb_info(self, package_path):
        """Get information from .deb package"""
        try:
            result = subprocess.run(
                ['dpkg-deb', '-I', package_path],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                # Parse and format the output
                info = result.stdout
                lines = info.split('\n')
                
                # Extract key information
                formatted_info = "Package Type: Debian (.deb)\n\n"
                for line in lines:
                    line = line.strip()
                    if line.startswith('Package:') or \
                       line.startswith('Version:') or \
                       line.startswith('Architecture:') or \
                       line.startswith('Maintainer:') or \
                       line.startswith('Description:'):
                        formatted_info += line + '\n'
                
                return formatted_info if formatted_info else info
            else:
                return f"Package Type: Debian (.deb)\n\nFilename: {os.path.basename(package_path)}\nSize: {self._get_file_size(package_path)}"
        except FileNotFoundError:
            return f"Package Type: Debian (.deb)\n\nFilename: {os.path.basename(package_path)}\nSize: {self._get_file_size(package_path)}\n\nNote: dpkg-deb not found. Install dpkg for detailed info."
        except Exception as e:
            return f"Package Type: Debian (.deb)\n\nError: {str(e)}"
    
    def _get_rpm_info(self, package_path):
        """Get information from .rpm package"""
        try:
            result = subprocess.run(
                ['rpm', '-qip', package_path],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                # Parse and format the output
                info = result.stdout
                lines = info.split('\n')
                
                # Extract key information
                formatted_info = "Package Type: RPM\n\n"
                for line in lines:
                    line = line.strip()
                    if line.startswith('Name') or \
                       line.startswith('Version') or \
                       line.startswith('Release') or \
                       line.startswith('Architecture') or \
                       line.startswith('Summary') or \
                       line.startswith('Description'):
                        formatted_info += line + '\n'
                
                return formatted_info if formatted_info else info
            else:
                return f"Package Type: RPM\n\nFilename: {os.path.basename(package_path)}\nSize: {self._get_file_size(package_path)}"
        except FileNotFoundError:
            return f"Package Type: RPM\n\nFilename: {os.path.basename(package_path)}\nSize: {self._get_file_size(package_path)}\n\nNote: rpm not found. Install rpm for detailed info."
        except Exception as e:
            return f"Package Type: RPM\n\nError: {str(e)}"
    
    def _get_file_size(self, file_path):
        """Get file size in human-readable format"""
        size_bytes = os.path.getsize(file_path)
        
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        
        return f"{size_bytes:.2f} TB"
    
    def install_package(self, package_path):
        """Install the package using appropriate package manager"""
        package_type = self.get_package_type(package_path)
        
        try:
            if package_type == '.deb':
                return self._install_deb(package_path)
            elif package_type == '.rpm':
                return self._install_rpm(package_path)
            else:
                return False, "Unsupported package format"
        except Exception as e:
            return False, f"Installation failed: {str(e)}"
    
    def _install_deb(self, package_path):
        """Install .deb package"""
        try:
            # Try using apt first (handles dependencies better)
            if self._command_exists('apt'):
                result = subprocess.run(
                    ['pkexec', 'apt', 'install', '-y', package_path],
                    capture_output=True,
                    text=True,
                    timeout=300
                )
            # Fallback to dpkg
            elif self._command_exists('dpkg'):
                result = subprocess.run(
                    ['pkexec', 'dpkg', '-i', package_path],
                    capture_output=True,
                    text=True,
                    timeout=300
                )
                
                # Fix dependencies if needed
                if result.returncode != 0:
                    subprocess.run(
                        ['pkexec', 'apt-get', 'install', '-f', '-y'],
                        timeout=300
                    )
            else:
                return False, "No suitable package manager found for .deb files"
            
            if result.returncode == 0:
                return True, f"Package installed successfully!\n\n{result.stdout}"
            else:
                error_msg = result.stderr if result.stderr else result.stdout
                return False, f"Installation failed:\n{error_msg}"
                
        except subprocess.TimeoutExpired:
            return False, "Installation timed out. The package may be too large or there may be network issues."
        except Exception as e:
            return False, f"Installation error: {str(e)}"
    
    def _install_rpm(self, package_path):
        """Install .rpm package"""
        try:
            # Try DNF first (Fedora)
            if self._command_exists('dnf'):
                result = subprocess.run(
                    ['pkexec', 'dnf', 'install', '-y', package_path],
                    capture_output=True,
                    text=True,
                    timeout=300
                )
            # Try YUM (RHEL/CentOS)
            elif self._command_exists('yum'):
                result = subprocess.run(
                    ['pkexec', 'yum', 'install', '-y', package_path],
                    capture_output=True,
                    text=True,
                    timeout=300
                )
            # Try Zypper (openSUSE)
            elif self._command_exists('zypper'):
                result = subprocess.run(
                    ['pkexec', 'zypper', 'install', '-y', package_path],
                    capture_output=True,
                    text=True,
                    timeout=300
                )
            # Fallback to rpm
            elif self._command_exists('rpm'):
                result = subprocess.run(
                    ['pkexec', 'rpm', '-ivh', package_path],
                    capture_output=True,
                    text=True,
                    timeout=300
                )
            else:
                return False, "No suitable package manager found for .rpm files"
            
            if result.returncode == 0:
                return True, f"Package installed successfully!\n\n{result.stdout}"
            else:
                error_msg = result.stderr if result.stderr else result.stdout
                return False, f"Installation failed:\n{error_msg}"
                
        except subprocess.TimeoutExpired:
            return False, "Installation timed out. The package may be too large or there may be network issues."
        except Exception as e:
            return False, f"Installation error: {str(e)}"
    
    def check_permissions(self):
        """Check if the user has necessary permissions"""
        # Check if running as root or can use sudo/pkexec
        if os.geteuid() == 0:
            return True
        
        # Check for pkexec
        if self._command_exists('pkexec'):
            return True
        
        # Check for sudo
        if self._command_exists('sudo'):
            return True
        
        return False
