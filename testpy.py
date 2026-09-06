import numpy as np
import matplotlib.pyplot as plt


def main():
    # ==============================
    # 1. Thiết lập tham số
    # ==============================

    t = np.linspace(0, 12, 1200)

    A = 6.0
    beta = 0.25
    frequency = 0.8
    omega = 2 * np.pi * frequency
    phi = np.pi / 6

    # ==============================
    # 2. Đường bao dao động
    # ==============================

    envelope = A * np.exp(-beta * t)

    # ==============================
    # 3. Tín hiệu lý thuyết
    # ==============================

    x_ideal = envelope * np.cos(omega * t + phi)

    # ==============================
    # 4. Thêm nhiễu Gaussian
    # ==============================

    np.random.seed(10)

    noise_std = 0.3

    noise = np.random.normal(
        0,
        noise_std,
        size=len(t)
    )

    x_noisy = x_ideal + noise

    # ==============================
    # 5. Vẽ đồ thị
    # ==============================

    plt.figure(figsize=(10, 6))

    plt.plot(
        t,
        x_noisy,
        alpha=0.5,
        linewidth=1,
        label="Dữ liệu cảm biến"
    )

    plt.plot(
        t,
        x_ideal,
        linewidth=2,
        label="Tín hiệu lý thuyết"
    )

    plt.plot(
        t,
        envelope,
        linestyle="--",
        linewidth=1.5,
        label="Đường bao"
    )

    plt.plot(
        t,
        -envelope,
        linestyle="--",
        linewidth=1.5
    )

    # ==============================
    # 6. Thiết lập biểu đồ
    # ==============================

    plt.title(
        "Mô phỏng dao động tắt dần có nhiễu Gaussian",
        fontsize=14
    )

    plt.xlabel(
        "Thời gian (s)",
        fontsize=12
    )

    plt.ylabel(
        "Biên độ",
        fontsize=12
    )

    plt.grid(
        True,
        linestyle="--",
        alpha=0.6
    )

    plt.legend()

    plt.tight_layout()

    # ==============================
    # 7. Lưu kết quả
    # ==============================

    output_img = "damped_oscillation_plot.png"

    plt.savefig(
        output_img,
        dpi=300
    )

    print(
        f"-> Đã xuất đồ thị thành công ra file: {output_img}"
    )


if __name__ == "__main__":
    main()