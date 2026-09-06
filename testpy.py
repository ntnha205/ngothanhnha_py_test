import numpy as np
import matplotlib.pyplot as plt


def main():
    # ==============================
    # 1. Thiết lập các tham số
    # ==============================

    # Thời gian mô phỏng
    t = np.linspace(0, 10, 1000)

    # Biên độ ban đầu
    A = 5.0

    # Hệ số suy giảm
    beta = 0.3

    # Tần số góc
    omega = 2 * np.pi * 1.0

    # Pha ban đầu
    phi = 0.0

    # ==============================
    # 2. Tạo đường bao dao động
    # ==============================

    envelope = A * np.exp(-beta * t)

    # ==============================
    # 3. Nghiệm lý thuyết
    # ==============================

    x_ideal = envelope * np.cos(omega * t + phi)

    # ==============================
    # 4. Thêm nhiễu Gaussian
    # ==============================

    np.random.seed(42)

    noise_std = 0.25

    noise = np.random.normal(
        0,
        noise_std,
        size=len(t)
    )

    # Dữ liệu có nhiễu
    x_noisy = x_ideal + noise

    # ==============================
    # 5. Vẽ biểu đồ
    # ==============================

    plt.figure(figsize=(10, 6))

    # Dữ liệu cảm biến có nhiễu
    plt.plot(
        t,
        x_noisy,
        alpha=0.5,
        linewidth=1,
        label="Dữ liệu cảm biến có nhiễu"
    )

    # Nghiệm lý thuyết
    plt.plot(
        t,
        x_ideal,
        linewidth=2,
        label="Nghiệm lý thuyết"
    )

    # Đường bao phía trên
    plt.plot(
        t,
        envelope,
        linestyle="--",
        linewidth=1.5,
        label="Đường bao"
    )

    # Đường bao phía dưới
    plt.plot(
        t,
        -envelope,
        linestyle="--",
        linewidth=1.5
    )

    # ==============================
    # 6. Trang trí biểu đồ
    # ==============================

    plt.title(
        "Mô phỏng dao động tắt dần có nhiễu Gaussian",
        fontsize=14
    )

    plt.xlabel(
        "Thời gian t (s)",
        fontsize=12
    )

    plt.ylabel(
        "Biên độ x(t)",
        fontsize=12
    )

    plt.grid(
        True,
        linestyle="--",
        alpha=0.6
    )

    plt.legend(
        loc="upper right",
        framealpha=0.9
    )

    plt.tight_layout()

    # ==============================
    # 7. Lưu biểu đồ
    # ==============================

    output_img = "damped_oscillation_plot.png"

    plt.savefig(
        output_img,
        dpi=300
    )

    print(
        f"-> Đã xuất đồ thị thành công ra file: {output_img}"
    )

    # ==============================
    # 8. Hiển thị biểu đồ
    # ==============================

    plt.show()


if __name__ == "__main__":
    main()