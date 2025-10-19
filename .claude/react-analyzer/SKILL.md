---
name: react-analyzer
description: Comprehensive React project analyzer that examines code structure, components, hooks, dependencies, and best practices. Use when analyzing React/Next.js projects for code review, architectural assessment, or generating technical reports. Creates detailed markdown reports with project metrics, component analysis, and improvement recommendations.
---

# React Analyzer

## Overview

Analyze React projects comprehensively and generate detailed markdown reports. This skill examines project structure, components, custom hooks, dependencies, and adherence to React best practices.

## Core Capabilities

### 1. Project Structure Analysis
- Scan and categorize React files (.js, .jsx, .ts, .tsx)
- Analyze package.json for project metadata and dependencies
- Generate file structure metrics and TypeScript adoption rates

### 2. Component Detection & Classification
- Identify function components and class components
- Extract component names, types, and locations
- Track component distribution across the codebase

### 3. Custom Hook Analysis
- Detect custom hooks following the "use" naming convention
- Map hook locations and usage patterns
- Assess code reusability through custom hooks

### 4. Dependencies & Ecosystem Analysis
- Categorize production vs development dependencies
- Identify React ecosystem libraries (Redux, Router, UI frameworks)
- Analyze dependency counts and potential bloat

### 5. Best Practices Assessment
- Evaluate TypeScript adoption
- Assess function vs class component usage
- Provide recommendations for modern React practices

### 6. Report Generation
- Create timestamped markdown reports in specified directory
- Include comprehensive metrics, tables, and recommendations
- Format: `{project_name}_react_analysis_{timestamp}.md`

## Quick Start

Analyze a React project and generate a report:

```python
# Run the analyzer script
python scripts/react_analyzer.py /path/to/react/project --output ./reports
```

## Workflow

### Step 1: Identify React Project
Verify the target directory contains a React project by checking:
- `package.json` exists with React dependencies
- Presence of React file extensions (.jsx, .tsx)
- Common React project structure

### Step 2: Deep Analysis
Run comprehensive analysis covering:
- Project metadata extraction
- File structure scanning  
- Component and hook detection
- Dependency analysis
- Best practices evaluation

### Step 3: Report Generation
Generate markdown report with:
- Project overview and metrics
- Detailed component and hook tables
- Dependency breakdown
- Best practices recommendations
- Issues and improvement suggestions

### Step 4: Output Organization
Save reports to organized directory structure:
```
reports/
└── {project_name}_react_analysis_{YYYYMMDD_HHMMSS}.md
```

## Usage Patterns

### Code Review & Assessment
```bash
# Analyze for code review
python scripts/react_analyzer.py ./src --output ./reviews
```

### Architecture Documentation  
```bash
# Generate architecture overview
python scripts/react_analyzer.py . --output ./docs/architecture
```

### Migration Planning
```bash
# Assess project for TypeScript migration
python scripts/react_analyzer.py . --output ./migration-analysis
```

## Resources

### Scripts
- `scripts/react_analyzer.py` - Main analysis script with full project scanning capabilities

### References  
- `references/api_reference.md` - Detailed analysis patterns and workflow documentation

### Assets
- `assets/report_template.md` - Markdown template for consistent report formatting

## Integration Examples

### With CI/CD Pipeline
Add React analysis to your build process:
```yaml
- name: Analyze React Code
  run: python react-analyzer/scripts/react_analyzer.py . --output ./reports
```

### With Development Workflow
Regular project health checks:
```bash
# Weekly analysis
python scripts/react_analyzer.py . --output ./reports/weekly
```

## Output Structure

Generated reports include:
- **Project Information**: Name, version, React version, description
- **Metrics Dashboard**: Component counts, TypeScript adoption, file statistics
- **Component Inventory**: Detailed table of all React components with locations
- **Custom Hooks**: List of reusable logic hooks
- **Dependencies**: Production and development dependency analysis
- **Best Practices**: Automated assessment with improvement recommendations
- **Issues**: Detected problems and potential improvements

Reports are timestamped and organized for easy tracking of project evolution over time.
