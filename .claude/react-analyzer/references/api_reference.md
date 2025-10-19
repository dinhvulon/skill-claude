# React Analysis Reference

## Phân tích cấu trúc dự án React

### Các thành phần được phân tích

#### 1. Thông tin dự án cơ bản
- Tên dự án, phiên bản từ package.json
- Phiên bản React đang sử dụng
- Mô tả dự án
- Scripts có sẵn

#### 2. Components
- **Function Components**: Các component được định nghĩa bằng function/const
- **Class Components**: Các component kế thừa từ React.Component
- Vị trí file và dòng code của từng component

#### 3. Custom Hooks
- Các hook tùy chỉnh (bắt đầu với "use")
- Vị trí trong codebase

#### 4. Dependencies
- Production dependencies
- Development dependencies  
- Các thư viện trong React ecosystem

#### 5. File Structure
- Số lượng file theo loại (.js, .jsx, .ts, .tsx, .css)
- Cấu trúc thư mục tổng quan

#### 6. Metrics & Best Practices
- Tỷ lệ sử dụng TypeScript
- Tỷ lệ Function vs Class components
- Các đề xuất cải thiện code

### Patterns nhận diện

#### Component Patterns
```javascript
// Function component
const MyComponent = () => { }
function MyComponent() { }
export const MyComponent = () => { }

// Class component  
class MyComponent extends Component { }
class MyComponent extends React.Component { }
```

#### Hook Patterns
```javascript
// Custom hooks
const useCustomHook = () => { }
function useMyHook() { }
export const useApiData = () => { }
```

### Output Report Structure

#### Sections trong report:
1. **Project Information** - Thông tin cơ bản về dự án
2. **Project Metrics** - Các chỉ số quan trọng
3. **File Structure Overview** - Tổng quan cấu trúc file
4. **Components** - Danh sách chi tiết các component
5. **Custom Hooks** - Danh sách các custom hook
6. **Dependencies** - Phân tích dependencies
7. **Best Practices Assessment** - Đánh giá best practices
8. **Issues Found** - Các vấn đề phát hiện được

### Recommended Analysis Workflow

1. **Xác định dự án React** - Kiểm tra package.json có React
2. **Quét cấu trúc file** - Đếm các loại file
3. **Phân tích components** - Tìm và phân loại components
4. **Phân tích hooks** - Tìm custom hooks
5. **Đánh giá best practices** - So sánh với chuẩn React
6. **Tạo report** - Xuất báo cáo markdown với timestamp
