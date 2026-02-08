# ✨ SnapWiz - Feature Roadmap v2.0

## New Features Implementation Plan

---

## 🎯 Feature List

### 6. Batch Installation
**Status**: 🚧 Planned  
**Priority**: High  
**Complexity**: Medium

**Description**: Allow users to select and install multiple packages at once

**Features**:
- Multi-file selection dialog
- Package queue display
- Sequential installation with progress tracking
- Cancel/pause queue functionality
- Estimated total time
- Skip failed packages option

**UI Changes**:
- Add "Add to Queue" button
- Display queue list with drag-to-reorder
- Show current installing package
- Queue progress bar (X of Y packages)

---

### 7. Uninstallation Feature
**Status**: 🚧 Planned  
**Priority**: High  
**Complexity**: Medium

**Description**: Remove installed packages through the GUI

**Features**:
- List all installed packages
- Filter by .deb or .rpm
- Search installed packages
- Uninstall with confirmation
- Dependency checking
- Uninstall history logging

**UI Changes**:
- New "Uninstall Package" tab
- Package list with search
- Uninstall button
- Confirmation dialog

**Backend**:
```bash
# Debian/Ubuntu
sudo apt remove package-name
sudo dpkg -r package-name

# Fedora/RHEL
sudo dnf remove package-name
sudo rpm -e package-name
```

---

### 8. Package Verification
**Status**: 🚧 Planned  
**Priority**: Medium  
**Complexity**: High

**Description**: Verify package integrity before installation

**Features**:
- SHA256 checksum verification
- MD5 checksum verification (fallback)
- GPG signature validation
- File size verification
- Verification status display
- Skip verification option

**UI Changes**:
- Verification step in progress
- Checksum input field
- "Verify Package" button
- Verification status indicator
- Trust/skip prompt for failed verification

**Implementation**:
```python
import hashlib
import gnupg  # for GPG

def verify_sha256(file_path, expected_hash):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest() == expected_hash
```

---

### 9. Search & Filter
**Status**: 🚧 Planned  
**Priority**: Medium  
**Complexity**: Low

**Description**: Enhanced history browsing capabilities

**Features**:
- Search by package name
- Filter by:
  - Status (Success/Failed)
  - Date range
  - Package type (.deb/.rpm)
- Sort by date/name/status
- Real-time search
- Clear filters button

**UI Changes**:
- Search bar in History tab
- Filter dropdown menus
- Sort options
- Result count display
- Highlight search matches

---

### 10. Export/Import History
**Status**: 🚧 Planned  
**Priority**: Low  
**Complexity**: Low

**Description**: Backup and analyze installation history

**Features**:
- Export to CSV format
- Export to JSON format
- Import history from backup
- Merge or replace option
- Export date selection
- Statistics in export

**UI Changes**:
- Export/Import buttons in History tab
- File format selection
- Date range selector
- Export confirmation

**Export Formats**:

**CSV**:
```csv
Timestamp,Package Name,Status,Message
2026-02-08 18:00:00,example.deb,Success,Installed successfully
```

**JSON**:
```json
{
  "export_date": "2026-02-08",
  "total_entries": 50,
  "entries": [...]
}
```

---

## 📋 Implementation Order

### Phase 1: Core Features (v1.1)
1. **Search & Filter** ⭐ (Quick win, high value)
2. **Export/Import History** ⭐ (Easy, useful)

### Phase 2: Advanced Features (v1.2)
3. **Batch Installation** ⭐⭐ (Complex queue system)
4. **Uninstallation Feature** ⭐⭐ (New tab, package listing)

### Phase 3: Security Features (v1.3)
5. **Package Verification** ⭐⭐⭐ (Security critical, complex)

---

## 🛠️ Technical Requirements

### Dependencies
```
# Current
PyQt5>=5.15.0

# New (for upcoming features)
python-gnupg>=0.4.8  # For GPG signature verification
```

### New Files
- `queue_manager.py` - Batch installation queue
- `package_verifier.py` - Checksum/signature verification
- `package_uninstaller.py` - Uninstall functionality

### Modified Files
- `main.py` - New UI tabs and features
- `logger.py` - Export/import functionality
- `package_handler.py` - Verification integration

---

## 🎨 UI Mockup Changes

### New Tabs
1. **Install Package** (existing, enhanced with queue)
2. **Uninstall Package** (NEW)
3. **Installation History** (existing, enhanced with search/filter)
4. **Settings** (existing)

### Install Tab Enhancements
```
┌─────────────────────────────────────────┐
│ 📦 Select Packages                      │
│ ┌─────────────────────────────────────┐ │
│ │ /path/to/package1.deb               │ │
│ └─────────────────────────────────────┘ │
│ [Browse...]  [Add to Queue]             │
│                                         │
│ 📋 Installation Queue (3 packages)      │
│ ┌─────────────────────────────────────┐ │
│ │ ✓ package1.deb                      │ │
│ │ ⏳ package2.deb (current)            │ │
│ │ ⏸ package3.rpm                       │ │
│ └─────────────────────────────────────┘ │
│ [Clear Queue]  [Start Installation]     │
└─────────────────────────────────────────┘
```

### Uninstall Tab (NEW)
```
┌─────────────────────────────────────────┐
│ 🗑️ Uninstall Package                    │
│                                         │
│ Search: [____________] 🔍               │
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │ □ apache2 (2.4.41)                  │ │
│ │ □ firefox (95.0.1)                  │ │
│ │ □ vim (8.2)                         │ │
│ │ ...                                 │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ [Refresh List]  [Uninstall Selected]    │
└─────────────────────────────────────────┘
```

### History Tab Enhancements
```
┌─────────────────────────────────────────┐
│ 📋 Installation History                 │
│                                         │
│ Search: [____________] 🔍               │
│ Filter: [All Status ▼] [All Types ▼]   │
│ Date: [Last 30 days ▼]                  │
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │ ✅ package.deb - 2026-02-08         │ │
│ │ ❌ failed.rpm - 2026-02-07          │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ [Export CSV] [Export JSON] [Import]     │
└─────────────────────────────────────────┘
```

---

## 📊 Feature Comparison

| Feature | v1.0 (Current) | v2.0 (Planned) |
|---------|----------------|----------------|
| Single Installation | ✅ | ✅ |
| Batch Installation | ❌ | ✅ |
| Uninstallation | ❌ | ✅ |
| Package Verification | ❌ | ✅ |
| History Viewing | ✅ | ✅ |
| Search History | ❌ | ✅ |
| Filter History | ❌ | ✅ |
| Export History | ❌ | ✅ |
| Import History | ❌ | ✅ |

---

## ⚠️ Considerations

### Batch Installation
- **Memory usage**: Large queues may consume memory
- **Error handling**: One failed package shouldn't stop queue
- **User experience**: Show clear progress for each package

### Uninstallation
- **Safety**: Always confirm before uninstalling
- **Dependencies**: Warn about dependency removals
- **System packages**: Prevent uninstalling critical packages

### Package Verification
- **Optional**: Don't force verification (some users won't have checksums)
- **Performance**: Don't slow down installation significantly
- **Trust model**: Allow users to proceed despite failed verification

### Search & Filter
- **Performance**: Optimize for large history files (1000+ entries)
- **UX**: Real-time search without lag

### Export/Import
- **Data integrity**: Validate imported data
- **Merge strategy**: Clear options for merge vs replace
- **Backup**: Don't overwrite existing history

---

## 🚀 Development Timeline

### Week 1: Foundation
- [ ] Create feature branch
- [ ] Design database schema updates
- [ ] Create new module files

### Week 2: Search & Filter
- [ ] Implement search functionality
- [ ] Add filter dropdowns
- [ ] Test with large datasets

### Week 3: Export/Import
- [ ] CSV export
- [ ] JSON export
- [ ] Import with validation
- [ ] Merge logic

### Week 4: Batch Installation
- [ ] Queue manager
- [ ] Sequential installation
- [ ] Progress tracking
- [ ] Error handling

### Week 5: Uninstallation
- [ ] Package listing
- [ ] Uninstall backend
- [ ] UI integration
- [ ] Safety checks

### Week 6: Package Verification
- [ ] Checksum verification
- [ ] GPG integration
- [ ] UI integration
- [ ] Optional verification flow

### Week 7: Testing & Polish
- [ ] Integration testing
- [ ] UI/UX refinement
- [ ] Documentation
- [ ] Release v2.0

---

## 📚 Documentation Updates Needed

- [ ] Update README with new features
- [ ] Update UI_UX_ENHANCEMENTS.md
- [ ] Create BATCH_INSTALLATION.md guide
- [ ] Create UNINSTALLATION.md guide
- [ ] Update KEYBOARD_SHORTCUTS.md
- [ ] Update CHANGELOG.md

---

## ✅ Success Criteria

### Batch Installation
- [ ] Can queue 10+ packages
- [ ] Can install sequentially
- [ ] Can cancel mid-queue
- [ ] Shows accurate progress

### Uninstallation
- [ ] Lists all installed packages
- [ ] Can search packages
- [ ] Can uninstall safely
- [ ] Logs uninstallations

### Package Verification
- [ ] Verifies SHA256
- [ ] Verifies GPG (if available)
- [ ] Shows clear status
- [ ] Allows skip

### Search & Filter
- [ ] Real-time search
- [ ] Filter by all criteria
- [ ] Sorts correctly
- [ ] Performs well (1000+ entries)

### Export/Import
- [ ] Exports to CSV
- [ ] Exports to JSON
- [ ] Imports without data loss
- [ ] Merge works correctly

---

**Last Updated**: 2026-02-08  
**Version**: 2.0 Roadmap  
**Status**: Planning Phase  
**Target Release**: TBD
