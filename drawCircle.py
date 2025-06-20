import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def draw (R, w0, b):
	t_vals = np.linspace(0, 2*np.pi, 300)

	fig, ax = plt.subplots()
	ax.set_aspect("equal")
	ax.grid(True)
	ax.set_title("Chuyển động tròn biến đổi đều")

	theta = np.linspace(0, 2*np.pi, 300)
	ax.plot(R * np.cos(theta), R * np.sin(theta), "lightgray", label="Quỹ đạo")

	ax.plot([0], [0], "bo", label="Tâm")

	point, = ax.plot([], [], "ro", label="Chất điểm")

	txt_speed = ax.text(-R, R, "", fontsize=10)

	def update(frame):
		t = t_vals[frame]
		x = R * np.cos(w0*t + 0.5*b*t*t)
		y = R * np.sin(w0*t + 0.5*b*t*t)
		v = R*(w0 + b*t)
		point.set_data([x], [y])
		txt_speed.set_text(f"Tốc độ: {v:.2f}m/s")
		return point,txt_speed

	ani = FuncAnimation(fig, update, frames=len(t_vals), interval=20, blit=True, repeat=False)


	plt.legend(loc="upper right")
	plt.show()

def main():
	R = 10
	w = 0
	b = 10

	draw(R, w, b)

if __name__ == "__main__":
	main()

