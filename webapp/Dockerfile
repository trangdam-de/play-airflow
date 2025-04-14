# Sử dụng image gốc Python phiên bản 3.9 từ Docker Hub
FROM python:3.9
# Thiết lập thư mục làm việc trong container là thư mục hiện tại
WORKDIR ./
# Sao chép file requirements.txt từ máy host vào container
COPY requirements.txt .
# Cài đặt các gói phụ thuộc từ requirements.txt và sau đó xóa file này để giảm kích thước image
RUN pip install -r requirements.txt && rm -f requirements.txt
# Cài đặt markupsafe phiên bản 2.0.1 để giải quyết vấn đề tương thích với Flask 1.1.4
# Flask 1.1.4 yêu cầu markupsafe có hàm soft_unicode, chỉ có trong phiên bản cũ hơn
RUN pip install markupsafe==2.0.1
# Sao chép file app.py từ máy host vào container
COPY app.py .
# Khai báo rằng container sẽ lắng nghe trên cổng 5000
EXPOSE 5000
# Định nghĩa lệnh mặc định khi container được khởi chạy
# Trong trường hợp này, chạy ứng dụng Flask với Python
CMD python app.py