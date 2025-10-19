#!/usr/bin/env python3
"""
React code analyzer script that analyzes React project structure, 
components, hooks, dependencies, and generates comprehensive reports.
"""

import os
import json
import ast
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Any, Optional
import argparse

class ReactAnalyzer:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.analysis_results = {
            'project_info': {},
            'components': [],
            'hooks': [],
            'dependencies': {},
            'file_structure': {},
            'issues': [],
            'metrics': {},
            'best_practices': []
        }
        
    def analyze(self) -> Dict[str, Any]:
        """Main analysis method"""
        print(f"🔍 Analyzing React project at: {self.project_path}")
        
        self._analyze_project_info()
        self._analyze_dependencies()
        self._analyze_file_structure()
        self._scan_react_files()
        self._analyze_metrics()
        self._check_best_practices()
        
        return self.analysis_results
    
    def _analyze_project_info(self):
        """Analyze basic project information"""
        package_json = self.project_path / 'package.json'
        if package_json.exists():
            try:
                with open(package_json, 'r', encoding='utf-8') as f:
                    package_data = json.load(f)
                    self.analysis_results['project_info'] = {
                        'name': package_data.get('name', 'Unknown'),
                        'version': package_data.get('version', 'Unknown'),
                        'description': package_data.get('description', ''),
                        'react_version': package_data.get('dependencies', {}).get('react', 'Unknown'),
                        'scripts': package_data.get('scripts', {}),
                        'author': package_data.get('author', 'Unknown')
                    }
            except Exception as e:
                self.analysis_results['issues'].append(f"Error reading package.json: {e}")
        else:
            self.analysis_results['issues'].append("package.json not found")
    
    def _analyze_dependencies(self):
        """Analyze project dependencies"""
        package_json = self.project_path / 'package.json'
        if package_json.exists():
            try:
                with open(package_json, 'r', encoding='utf-8') as f:
                    package_data = json.load(f)
                    deps = package_data.get('dependencies', {})
                    dev_deps = package_data.get('devDependencies', {})
                    
                    self.analysis_results['dependencies'] = {
                        'production': deps,
                        'development': dev_deps,
                        'total_count': len(deps) + len(dev_deps),
                        'react_ecosystem': self._identify_react_ecosystem_deps(deps)
                    }
            except Exception as e:
                self.analysis_results['issues'].append(f"Error analyzing dependencies: {e}")
    
    def _identify_react_ecosystem_deps(self, deps: Dict[str, str]) -> List[str]:
        """Identify React ecosystem dependencies"""
        react_deps = []
        react_keywords = ['react', 'redux', 'router', 'styled', 'material-ui', 'antd', 'chakra']
        
        for dep in deps:
            if any(keyword in dep.lower() for keyword in react_keywords):
                react_deps.append(dep)
        
        return react_deps
    
    def _analyze_file_structure(self):
        """Analyze project file structure"""
        structure = {}
        js_files = 0
        jsx_files = 0
        ts_files = 0
        tsx_files = 0
        css_files = 0
        
        for root, dirs, files in os.walk(self.project_path):
            # Skip node_modules and other common directories
            dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'build', 'dist', '.next']]
            
            rel_root = os.path.relpath(root, self.project_path)
            structure[rel_root] = files
            
            for file in files:
                if file.endswith('.js'):
                    js_files += 1
                elif file.endswith('.jsx'):
                    jsx_files += 1
                elif file.endswith('.ts'):
                    ts_files += 1
                elif file.endswith('.tsx'):
                    tsx_files += 1
                elif file.endswith(('.css', '.scss', '.sass', '.less')):
                    css_files += 1
        
        self.analysis_results['file_structure'] = {
            'structure': structure,
            'file_counts': {
                'js': js_files,
                'jsx': jsx_files,
                'ts': ts_files,
                'tsx': tsx_files,
                'css': css_files
            }
        }
    
    def _scan_react_files(self):
        """Scan React files for components and hooks"""
        react_extensions = ['.js', '.jsx', '.ts', '.tsx']
        
        for root, dirs, files in os.walk(self.project_path):
            dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'build', 'dist', '.next']]
            
            for file in files:
                if any(file.endswith(ext) for ext in react_extensions):
                    file_path = Path(root) / file
                    self._analyze_react_file(file_path)
    
    def _analyze_react_file(self, file_path: Path):
        """Analyze individual React file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            rel_path = file_path.relative_to(self.project_path)
            
            # Find React components
            components = self._find_components(content, str(rel_path))
            self.analysis_results['components'].extend(components)
            
            # Find custom hooks
            hooks = self._find_hooks(content, str(rel_path))
            self.analysis_results['hooks'].extend(hooks)
            
        except Exception as e:
            self.analysis_results['issues'].append(f"Error analyzing {file_path}: {e}")
    
    def _find_components(self, content: str, file_path: str) -> List[Dict[str, Any]]:
        """Find React components in file content"""
        components = []
        
        # Pattern for function components (more comprehensive)
        patterns = [
            # const ComponentName = () => {
            r'(?:export\s+(?:default\s+)?)?const\s+([A-Z]\w*)\s*=\s*\([^)]*\)\s*=>\s*{',
            # function ComponentName() {
            r'(?:export\s+(?:default\s+)?)?function\s+([A-Z]\w*)\s*\([^)]*\)\s*{',
            # export default function ComponentName() {
            r'export\s+default\s+function\s+([A-Z]\w*)\s*\([^)]*\)\s*{',
            # const ComponentName: React.FC = () => {
            r'(?:export\s+(?:default\s+)?)?const\s+([A-Z]\w*)\s*:\s*[^=]*=\s*\([^)]*\)\s*=>\s*{',
        ]
        
        # Pattern for class components
        class_pattern = r'class\s+([A-Z]\w*)\s+extends\s+(?:React\.)?Component'
        
        for pattern in patterns:
            for match in re.finditer(pattern, content):
                component_name = match.group(1)
                components.append({
                    'name': component_name,
                    'type': 'function',
                    'file': file_path,
                    'line': content[:match.start()].count('\n') + 1
                })
        
        for match in re.finditer(class_pattern, content):
            component_name = match.group(1)
            components.append({
                'name': component_name,
                'type': 'class',
                'file': file_path,
                'line': content[:match.start()].count('\n') + 1
            })
        
        return components
    
    def _find_hooks(self, content: str, file_path: str) -> List[Dict[str, Any]]:
        """Find custom hooks in file content"""
        hooks = []
        
        # Pattern for custom hooks (functions starting with 'use')
        patterns = [
            # export const useHookName = () => {
            r'(?:export\s+(?:const\s+)?)?(use[A-Z]\w*)\s*=\s*\([^)]*\)\s*=>\s*{',
            # function useHookName() {
            r'(?:export\s+)?function\s+(use[A-Z]\w*)\s*\([^)]*\)\s*{',
            # export function useHookName() {
            r'export\s+function\s+(use[A-Z]\w*)\s*\([^)]*\)\s*{',
            # const useHookName: () => 
            r'(?:export\s+(?:const\s+)?)?(use[A-Z]\w*)\s*:\s*[^=]*=\s*\([^)]*\)\s*=>\s*{',
        ]
        
        for pattern in patterns:
            for match in re.finditer(pattern, content):
                hook_name = match.group(1)
                hooks.append({
                    'name': hook_name,
                    'file': file_path,
                    'line': content[:match.start()].count('\n') + 1
                })
        
        return hooks
    
    def _analyze_metrics(self):
        """Calculate project metrics"""
        self.analysis_results['metrics'] = {
            'total_components': len(self.analysis_results['components']),
            'function_components': len([c for c in self.analysis_results['components'] if c['type'] == 'function']),
            'class_components': len([c for c in self.analysis_results['components'] if c['type'] == 'class']),
            'custom_hooks': len(self.analysis_results['hooks']),
            'total_files': sum(self.analysis_results['file_structure']['file_counts'].values()),
            'typescript_adoption': (
                self.analysis_results['file_structure']['file_counts']['ts'] + 
                self.analysis_results['file_structure']['file_counts']['tsx']
            ) / max(sum(self.analysis_results['file_structure']['file_counts'].values()), 1) * 100
        }
    
    def _check_best_practices(self):
        """Check for React best practices"""
        practices = []
        
        # Check TypeScript adoption
        if self.analysis_results['metrics']['typescript_adoption'] > 50:
            practices.append("✅ Good TypeScript adoption")
        else:
            practices.append("⚠️ Consider adopting TypeScript for better type safety")
        
        # Check component types
        func_ratio = self.analysis_results['metrics']['function_components'] / max(self.analysis_results['metrics']['total_components'], 1)
        if func_ratio > 0.8:
            practices.append("✅ Good use of function components")
        else:
            practices.append("⚠️ Consider migrating class components to function components")
        
        # Check for custom hooks
        if self.analysis_results['metrics']['custom_hooks'] > 0:
            practices.append("✅ Using custom hooks for logic reuse")
        else:
            practices.append("💡 Consider creating custom hooks for reusable logic")
        
        self.analysis_results['best_practices'] = practices

def generate_report(analysis_results: Dict[str, Any], output_dir: str, project_name: str) -> str:
    """Generate markdown report"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"{project_name}_react_analysis_{timestamp}.md"
    report_path = Path(output_dir) / report_filename
    
    os.makedirs(output_dir, exist_ok=True)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# React Project Analysis Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Project Info
        f.write("## 📋 Project Information\n\n")
        project_info = analysis_results['project_info']
        f.write(f"- **Name:** {project_info.get('name', 'Unknown')}\n")
        f.write(f"- **Version:** {project_info.get('version', 'Unknown')}\n")
        f.write(f"- **React Version:** {project_info.get('react_version', 'Unknown')}\n")
        f.write(f"- **Description:** {project_info.get('description', 'N/A')}\n\n")
        
        # Metrics
        f.write("## 📊 Project Metrics\n\n")
        metrics = analysis_results['metrics']
        f.write(f"- **Total Components:** {metrics['total_components']}\n")
        f.write(f"- **Function Components:** {metrics['function_components']}\n")
        f.write(f"- **Class Components:** {metrics['class_components']}\n")
        f.write(f"- **Custom Hooks:** {metrics['custom_hooks']}\n")
        f.write(f"- **TypeScript Adoption:** {metrics['typescript_adoption']:.1f}%\n")
        f.write(f"- **Total Files:** {metrics['total_files']}\n\n")
        
        # File Structure
        f.write("## 📁 File Structure Overview\n\n")
        file_counts = analysis_results['file_structure']['file_counts']
        f.write(f"- **JavaScript Files:** {file_counts['js']}\n")
        f.write(f"- **JSX Files:** {file_counts['jsx']}\n")
        f.write(f"- **TypeScript Files:** {file_counts['ts']}\n")
        f.write(f"- **TSX Files:** {file_counts['tsx']}\n")
        f.write(f"- **CSS Files:** {file_counts['css']}\n\n")
        
        # Components
        f.write("## 🧩 Components\n\n")
        if analysis_results['components']:
            f.write("| Component | Type | File | Line |\n")
            f.write("|-----------|------|------|------|\n")
            for comp in analysis_results['components']:
                f.write(f"| {comp['name']} | {comp['type']} | {comp['file']} | {comp['line']} |\n")
        else:
            f.write("No React components found.\n")
        f.write("\n")
        
        # Hooks
        f.write("## 🪝 Custom Hooks\n\n")
        if analysis_results['hooks']:
            f.write("| Hook | File | Line |\n")
            f.write("|------|------|------|\n")
            for hook in analysis_results['hooks']:
                f.write(f"| {hook['name']} | {hook['file']} | {hook['line']} |\n")
        else:
            f.write("No custom hooks found.\n")
        f.write("\n")
        
        # Dependencies
        f.write("## 📦 Dependencies\n\n")
        deps = analysis_results['dependencies']
        f.write(f"**Total Dependencies:** {deps.get('total_count', 0)}\n\n")
        f.write("### React Ecosystem Dependencies\n")
        react_deps = deps.get('react_ecosystem', [])
        if react_deps:
            for dep in react_deps:
                f.write(f"- {dep}\n")
        else:
            f.write("No React ecosystem dependencies found.\n")
        f.write("\n")
        
        # Best Practices
        f.write("## 💡 Best Practices Assessment\n\n")
        for practice in analysis_results['best_practices']:
            f.write(f"{practice}\n\n")
        
        # Issues
        if analysis_results['issues']:
            f.write("## ⚠️ Issues Found\n\n")
            for issue in analysis_results['issues']:
                f.write(f"- {issue}\n")
            f.write("\n")
    
    return str(report_path)

def main():
    parser = argparse.ArgumentParser(description='Analyze React project')
    parser.add_argument('project_path', help='Path to React project')
    parser.add_argument('--output', '-o', default='./reports', help='Output directory for reports')
    
    args = parser.parse_args()
    
    analyzer = ReactAnalyzer(args.project_path)
    results = analyzer.analyze()
    
    project_name = results['project_info'].get('name', 'unknown-project')
    report_path = generate_report(results, args.output, project_name)
    
    print(f"✅ Analysis complete! Report saved to: {report_path}")

if __name__ == "__main__":
    main()
