# Báo cáo Kiểm thử Hiệu năng với JMeter

## Mục tiêu

Kiểm thử hiệu năng trang web Messenger Clone (`https://messenger-fe-eight.vercel.app`) để đánh giá khả năng chịu tải và độ ổn định.

## Môi trường kiểm thử

- **Website mục tiêu:** <https://messenger-fe-eight.vercel.app>
- **Công cụ:** Apache JMeter 5.6.3
- **Thời gian thực hiện:** 2026-01-19

## Kịch bản kiểm thử (Test Plan)

### Thread Group 1: Kịch bản cơ bản

- **Số lượng người dùng (Threads):** 10
- **Thời gian chạy (Loop Count):** 5 lần lặp
- **Hành vi:** Gửi yêu cầu HTTP GET đến trang chủ (`/`).
- **Mục đích:** Kiểm tra phản hồi cơ bản của hệ thống với tải thấp.

### Thread Group 2: Kịch bản tải nặng

- **Số lượng người dùng (Threads):** 50
- **Ramp-up Period:** 30 giây
- **Hành vi:**
  - GET `/`
  - GET `/login`
- **Mục đích:** Kiểm tra khả năng chịu tải khi người dùng tăng dần và truy cập nhiều trang.

### Thread Group 3: Kịch bản tùy chỉnh (Stress Test thời gian thực)

- **Số lượng người dùng (Threads):** 20
- **Thời gian chạy:** 60 giây (Scheduler enabled)
- **Hành vi:**
  - GET `/`
  - GET `/login`
- **Mục đích:** Kiểm tra độ ổn định của hệ thống trong một khoảng thời gian duy trì.

## Kết quả kiểm thử

Tổng quan: Đã thực hiện 4034 requests trong khoảng 60 giây.

### Tóm tắt (Summary Report)

| Kịch bản | Samples | Avg Time (ms) | Min (ms) | Max (ms) | Error % |
|----------|---------|---------------|----------|----------|---------|
| **Group 1 - Basic** | 50 | 539.02 | 128 | 1893 | 0.00% |
| **Group 2 - Heavy** | 100 | 474.85 | 140 | 1891 | 0.00% |
| **Group 3 - Custom** | 3884 | 285.00 | 112 | 1893 | 0.00% |

### Phân tích chi tiết

- **Độ ổn định:** Hệ thống hoạt động rất ổn định với **0% lỗi** trong tất cả các kịch bản.
- **Thời gian phản hồi:**
  - Trung bình, hệ thống phản hồi trong khoảng **~285ms - 539ms**.
  - Thời gian phản hồi thấp nhất là 112ms.
  - Thời gian phản hồi cao nhất (max) khoảng 1.8s (có thể do network latency hoặc initial connection handshake).
- **Khả năng chịu tải:**
  - Ở kịch bản tải nặng (50 users), hệ thống vẫn duy trì response time trung bình dưới 500ms.
  - Ở kịch bản chạy liên tục (Group 3), hệ thống xử lý ổn định ~60 req/s mà không gặp lỗi.

## Kết luận

Website `https://messenger-fe-eight.vercel.app` đáp ứng tốt các yêu cầu về hiệu năng cho mức tải được kiểm thử (lên đến 50 người dùng đồng thời). Không phát hiện lỗi HTTP 5xx hay 4xx trong quá trình test.

## Phụ lục

- File cấu hình: `performance_test.jmx`
- File kết quả thô: `results.csv`
- Báo cáo chi tiết HTML: Xem thư mục `dashboard/` (Mở `dashboard/index.html` để xem biểu đồ).
