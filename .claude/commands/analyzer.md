---
description: Run comprehensive code analysis and generate Markdown reports for security, performance, and quality assessment. Analyzes Python and React/JS/TS code with detailed findings and actionable recommendations.
---

# Smart Code Analyzer - Command Guide

## Overview

Smart Code Analyzer is a comprehensive static analysis tool that examines code for security vulnerabilities, performance bottlenecks, and quality issues. It supports both **Python** and **React/JavaScript/TypeScript** projects and generates professional Markdown reports.

---

## Quick Start

### Analyze and Generate Report (One Command)

```bash
# React/JS/TS Analysis
cd .claude/smart-code-analyzer/scripts
python react_performance_analyzer.py ../../../src > analysis.json
python generate_md_report.py analysis.json report.md react-performance

# Python Analysis
cd .claude/smart-code-analyzer/scripts
python performance_analyzer.py ../../../backend > analysis.json
python generate_md_report.py analysis.json report.md performance
```

---

## Available Analyzers

### 1. **React/JavaScript/TypeScript Analyzers**

#### a) React Performance Analyzer
**File:** `react_performance_analyzer.py`

**Detects:**
- Unnecessary re-renders
- Missing React.memo usage
- Missing useMemo/useCallback
- Inefficient loops (chained maps, filter+map)
- Memory leaks (setInterval, addEventListener)
- Heavy imports (lodash, moment)
- Large bundle issues
- Inline functions in JSX

**Usage:**
```bash
python react_performance_analyzer.py <project_path> > output.json
```

**Example:**
```bash
python react_performance_analyzer.py ../../../src/components > react_perf.json
python generate_md_report.py react_perf.json react_perf_report.md react-performance
```

---

#### b) React Security Analyzer
**File:** `react_security_analyzer.py`

**Detects:**
- XSS via dangerouslySetInnerHTML
- Hardcoded API keys and secrets
- Unsafe URL handling
- CORS issues
- localStorage security issues
- Missing input validation

**Usage:**
```bash
python react_security_analyzer.py <project_path> > output.json
python generate_md_report.py output.json report.md react-security
```

---

#### c) React Quality Analyzer
**File:** `react_quality_analyzer.py`

**Detects:**
- React best practices violations
- Accessibility issues
- Prop validation missing
- Poor component structure
- Anti-patterns
- JSX quality issues

**Usage:**
```bash
python react_quality_analyzer.py <project_path> > output.json
python generate_md_report.py output.json report.md react-quality
```

---

### 2. **Python Analyzers**

#### a) Python Performance Analyzer
**File:** `performance_analyzer.py`

**Detects:**
- Inefficient loops (range(len()))
- String concatenation issues
- Memory inefficiencies
- Complexity issues
- Algorithm optimization opportunities

**Usage:**
```bash
python performance_analyzer.py <project_path> > output.json
python generate_md_report.py output.json report.md performance
```

---

#### b) Python Security Analyzer
**File:** `security_analyzer.py`

**Detects:**
- SQL Injection
- Command Injection
- Path Traversal
- Hardcoded secrets
- Dangerous functions (eval, exec)

**Usage:**
```bash
python security_analyzer.py <project_path> > output.json
python generate_md_report.py output.json report.md security
```

---

#### c) Python Quality Analyzer
**File:** `code_quality_analyzer.py`

**Detects:**
- PEP 8 violations
- Missing docstrings
- Function complexity
- Code smells
- Naming conventions

**Usage:**
```bash
python code_quality_analyzer.py <project_path> > output.json
python generate_md_report.py output.json report.md quality
```

---

## Report Generator

### Markdown Report Generator
**File:** `generate_md_report.py`

**Usage:**
```bash
python generate_md_report.py <input_json> [output_md] [analysis_type]
```

**Parameters:**
- `input_json`: JSON output from any analyzer (required)
- `output_md`: Output Markdown file (default: `analysis_report.md`)
- `analysis_type`: Type of analysis (default: `general`)

**Analysis Types:**
- `security` - Security analysis
- `performance` - Performance analysis
- `quality` - Quality analysis
- `react-security` - React security
- `react-performance` - React performance
- `react-quality` - React quality
- `general` - General analysis

**Example:**
```bash
python generate_md_report.py analysis.json my_report.md react-performance
```

---

## Report Features

### What's Included in Reports:

1. **Executive Summary**
   - Code health status (Excellent/Good/Needs Attention/Critical)
   - Total issues count
   - Severity breakdown (High/Medium/Low)
   - Key metrics

2. **Summary Statistics**
   - Files analyzed
   - Lines of code
   - Functions and classes count
   - Complexity scores

3. **Severity Breakdown**
   - Visual progress bars
   - Percentage distribution
   - Color-coded priorities

4. **Category Breakdown**
   - Issues grouped by category
   - Icon indicators
   - Sortable table

5. **Detailed Issues**
   - File location with line numbers
   - Code snippets
   - Impact description
   - Actionable suggestions

6. **Recommendations**
   - Priority actions
   - Best practices
   - Next steps

---

## Common Workflows

### Workflow 1: Full Project Analysis

```bash
cd .claude/smart-code-analyzer/scripts

# Step 1: Run all React analyzers
python react_performance_analyzer.py ../../../src > react_perf.json
python react_security_analyzer.py ../../../src > react_sec.json
python react_quality_analyzer.py ../../../src > react_qual.json

# Step 2: Generate reports
python generate_md_report.py react_perf.json reports/performance.md react-performance
python generate_md_report.py react_sec.json reports/security.md react-security
python generate_md_report.py react_qual.json reports/quality.md react-quality
```

---

### Workflow 2: Quick Component Check

```bash
cd .claude/smart-code-analyzer/scripts

# Analyze specific component
python react_performance_analyzer.py ../../../src/components/Layout > layout_analysis.json

# Generate report
python generate_md_report.py layout_analysis.json layout_report.md react-performance

# View report
cat layout_report.md
```

---

### Workflow 3: CI/CD Integration

```bash
#!/bin/bash
# analyze.sh - Run in CI pipeline

cd .claude/smart-code-analyzer/scripts

# Run analysis
python react_performance_analyzer.py ../../../src > /tmp/analysis.json

# Generate report
python generate_md_report.py /tmp/analysis.json /tmp/report.md react-performance

# Check for critical issues
CRITICAL_ISSUES=$(jq '.summary.severity_breakdown.high' /tmp/analysis.json)

if [ "$CRITICAL_ISSUES" -gt 5 ]; then
  echo "FAILED: Too many critical issues ($CRITICAL_ISSUES)"
  exit 1
fi

echo "PASSED: Analysis complete"
```

---

## Output Examples

### Console Output
```
[OK] Markdown report generated: sidebar_analysis_report.md
[INFO] Analysis type: react-performance
[INFO] Total issues: 13
```

### Report Sample

See generated report at: `.claude/smart-code-analyzer/scripts/sidebar_analysis_report.md`

Key sections:
- 🔴 **1 High Priority** - Memory leaks (setTimeout cleanup)
- 🟡 **8 Medium Priority** - Missing React.memo, heavy imports
- 🟢 **4 Low Priority** - Inline functions, large files

---

## Best Practices

### 1. Regular Analysis
- Run analysis before commits
- Integrate into pre-commit hooks
- Schedule weekly full project scans

### 2. Prioritize Issues
- Fix HIGH severity first
- Address MEDIUM issues in sprints
- Track LOW issues as technical debt

### 3. Incremental Improvements
- Don't try to fix everything at once
- Set realistic goals per iteration
- Measure progress over time

### 4. Team Collaboration
- Share reports with team
- Discuss findings in code reviews
- Use as learning opportunities

---

## Troubleshooting

### Issue: Unicode errors on Windows
**Solution:** Fixed in v1.0.1 - uses ASCII-safe output

### Issue: Analysis too slow
**Solution:**
- Analyze specific directories instead of entire project
- Skip test files with proper .gitignore patterns
- Use `node_modules` exclusion patterns

### Issue: Too many issues reported
**Solution:**
- Focus on one analyzer at a time
- Set baseline and track improvements
- Use severity filters to prioritize

---

## File Structure

```
.claude/smart-code-analyzer/
├── scripts/
│   ├── react_performance_analyzer.py    # React perf analysis
│   ├── react_security_analyzer.py       # React security
│   ├── react_quality_analyzer.py        # React quality
│   ├── performance_analyzer.py          # Python perf
│   ├── security_analyzer.py             # Python security
│   ├── code_quality_analyzer.py         # Python quality
│   └── generate_md_report.py            # MD report generator ⭐
├── references/
│   ├── api_reference.md
│   ├── performance_guidelines.md
│   ├── quality_standards.md
│   ├── react_performance.md
│   └── react_security.md
├── assets/
│   └── report_template.html
└── SKILL.md
```

---

## Version History

**v1.0.1** (Current)
- ✅ Added Markdown report generator
- ✅ Fixed Unicode encoding issues
- ✅ Added detailed command documentation

**v1.0.0**
- Initial release with JSON output only

---

## Support & Resources

- **Documentation:** `.claude/smart-code-analyzer/references/`
- **Sample Reports:** `.claude/smart-code-analyzer/scripts/*.md`
- **Issue Tracking:** Create tasks based on report findings

---

*Last Updated: 2025-10-19*
