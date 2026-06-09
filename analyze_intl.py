"""International context figure: PISA math US vs OECD; TIMSS US math."""
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({
    "font.family": "serif", "font.size": 9, "axes.titlesize": 10,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.dpi": 150, "savefig.bbox": "tight",
})

pisa_years = [2003, 2006, 2009, 2012, 2015, 2018, 2022]
us_math = [483, 474, 487, 481, 470, 478, 465]
oecd_math = [500, 498, 496, 494, 490, 489, 472]
us_read_y = [2000, 2009, 2012, 2015, 2018, 2022]
us_read = [504, 500, 498, 497, 505, 504]
oecd_read_y = [2000, 2009, 2012, 2015, 2018, 2022]
oecd_read = [500, 493, 496, 493, 487, 476]

timss_years = [2011, 2015, 2019, 2023]
timss_g4 = [541, 539, 535, 517]
timss_g8 = [509, 518, 515, 488]

fig, axes = plt.subplots(1, 3, figsize=(8.5, 3))
ax = axes[0]
ax.plot(pisa_years, us_math, "-o", ms=3.5, color="#1f5fa8", label="United States")
ax.plot(pisa_years, oecd_math, "-s", ms=3.5, color="#b03a2e", label="OECD average")
ax.set_title("PISA mathematics, age 15")
ax.set_ylabel("PISA score")
ax.legend(frameon=False, fontsize=8)

ax = axes[1]
ax.plot(us_read_y, us_read, "-o", ms=3.5, color="#1f5fa8", label="United States")
ax.plot(oecd_read_y, oecd_read, "-s", ms=3.5, color="#b03a2e", label="OECD average")
ax.set_title("PISA reading, age 15")

ax = axes[2]
ax.plot(timss_years, timss_g4, "-o", ms=3.5, color="#1f5fa8", label="Grade 4")
ax.plot(timss_years, timss_g8, "-s", ms=3.5, color="#7fb0d8", label="Grade 8")
ax.set_title("TIMSS mathematics, U.S.")
ax.set_ylabel("TIMSS score")
ax.legend(frameon=False, fontsize=8)
fig.tight_layout()
fig.savefig("figures/fig_intl.pdf"); plt.close(fig)
print("intl figure done")
