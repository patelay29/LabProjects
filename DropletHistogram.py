

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm



# 20230623

radius =[[
    199.6362858, 205.586918, 193.1548363, 207.2126927, 207.7434205, 195.3226823,
    201.786209, 203.4185461, 207.2126927, 196.3957352, 219.6634283, 217.4811973,
    199.6362858, 193.1548363, 209.9381236, 193.1548363, 214.7855562, 203.4185461,
    212.6303755, 222.9100943, 205.586918, 195.3226823, 208.2817403, 203.4185461,
    197.485601, 192.6051923, 211.5445512, 207.2126927, 192.0403941, 194.2283538,
    216.9502452, 205.586918, 211.5445512, 195.3226823, 193.6817572, 193.6817572,
    211.5445512, 208.831, 195.836, 213.728, 202.884, 207.7435, 197.997,
    202.357, 213.13, 216.95, 198.5655, 210.4495, 211.011, 206.668,
    198.5655, 196.3955, 212.0715, 214.7855, 216.95, 199.6365, 190.982,
    191.538, 208.831, 205.587, 215.322, 195.3225, 202.357, 202.357,
    207.7435
],
[
    202.884, 219.6635, 207.2125, 208.831, 222.91, 191.538, 195.3225, 190.982, 191.538, 214.7855,
    186.111, 202.884, 239.1305, 228.837, 200.701, 243.9935, 197.4855, 174.2055, 218.0195, 181.8045,
    201.2785, 204.5185, 205.587, 188.8195, 297.5595, 174.7575, 213.728, 182.847, 196.933, 209.37,
    190.982, 174.7575, 188.281, 185.607, 191.538, 195.3225, 195.836, 192.0405, 197.4855, 206.668,
    189.89, 201.786, 201.2785, 223.9775, 239.1305, 201.786, 203.4185, 200.1985, 179.594, 190.4415,
    179.084, 200.701, 279.702, 227.7595, 209.938, 185.0145, 186.628, 198.5655, 187.735, 211.011,
    188.281, 244.542, 232.6345, 222.342, 278.098, 195.3225, 208.831, 199.067, 219.6635, 211.5445,
    198.5655, 194.7485, 219.6635, 202.884, 194.7485, 203.4185, 197.4855, 205.0435, 190.4415, 187.213,
    192.0405, 229.376, 190.4415, 186.111, 188.281, 194.7485, 232.1125, 196.933, 192.605, 290.5315,
    199.6365, 195.3225, 221.2935, 169.8865, 150.9415, 200.701, 142.269, 350.567, 207.7435, 193.155,
    189.3585, 188.281, 265.637, 195.836, 214.7855, 232.1125, 207.7435, 198.5655, 197.4855, 208.831,
    199.6365, 188.281, 185.0145, 239.6885, 206.668, 229.935, 198.5655, 212.0715, 204.5185, 180.6985,
    188.281, 200.701, 193.682, 223.432, 204.5185, 199.6365, 195.3225, 180.6985, 197.997, 202.357,
    227.2085, 212.6305, 196.3955, 190.4415, 247.7695, 205.587, 219.1175, 235.349, 194.7485, 192.605,
    195.836, 185.0145, 183.4095, 273.747, 224.5065, 191.538, 220.7465
]
]







flowrates = ["Test Sample1","Test Sample2"]
t10p = ['#1f77b4', '#2ca02c']

for i in radius:
    indLeg = radius.index(i)
    diameters = np.multiply(i, 2)
    # Fit a normal distribution to
    # the data:
    # mean and standard deviation
    mu, std = norm.fit(diameters)



    # Plot in Figure 1 (all together)
    plt.figure(1)
    # Plot the histogram.
    plt.hist(diameters, bins=20, density=True, alpha=0.5, color= t10p[indLeg])
    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, t10p[indLeg], linewidth=2)
    plt.axvline(x=mu,color= t10p[indLeg],linestyle='--', label='mean: %.0f \u03BCm' % mu + ', flowrate ratio ' + flowrates[indLeg])
    plt.title('Size Distributions, Normalized',fontweight='bold', fontsize=20)
    plt.ylabel('Normalized Count', fontsize=16)
    plt.xlabel('Droplet Diameter [\u03BCm]', fontsize=16)
    plot_title0 = plt.gca().get_title()
    filename0 = plot_title0.lower().replace(' ', '_') + '.png'


    ind = 3
    plt.figure(2)
    # Plot the histogram.
    plt.hist(diameters, bins=20, density=False, alpha=0.7, color= t10p[indLeg],label='flowrate ratio ' + flowrates[indLeg])
    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    #plt.plot(x, p, t10p[indLeg], linewidth=2)
    #plt.axvline(x=mu,color= t10p[indLeg],linestyle='--', label='mean: %.0f um' % mu + ', flowrate ratio ' + flowrates[indLeg])
    plt.title('Size Distributions',fontweight='bold', fontsize=20)
    plt.ylabel('Count', fontsize=16)
    plt.xlabel('Droplet Diameter [\u03BCm]', fontsize=16)
    plot_title1 = plt.gca().get_title()
    filename1 = plot_title1.lower().replace(' ', '_') + '.png'




    # Plot in separate Figures for each distribution
    plt.figure(ind + indLeg)
    # Plot the histogram.
    plt.hist(diameters, bins=20, density=True, alpha=0.5)
    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    plt.axvline(x=mu, linestyle='--', label='mean: %.0f \u03BCm, std: %.2f \u03BCm' % (mu,std))
    plt.title('Size Distribution, Flowrate Ratio ' + flowrates[indLeg] + ", N = {}".format(len(i)),fontweight='bold', fontsize=14)
    plt.xlim([(min(value for sublist in radius for value in sublist))*2 -50, (max(val for sub in radius for val in sub))*2 +50])
    plt.legend()
    plt.ylabel('Normalized Count', fontsize=12)
    plt.xlabel('Droplet Diameter [\u03BCm]',fontsize=12)
    plt.savefig("{}Normalized.png".format(ind + indLeg), dpi=300)


    plt.figure(ind+len(radius)+indLeg)
    plt.hist(diameters, bins=20, density=False, alpha = 0.8)
    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    #plt.plot(x, p, 'k', linewidth=2)
    plt.axvline(x=mu, linestyle='--', label='mean: %.0f \u03BCm, std: %.2f \u03BCm' % (mu,std))
    plt.title('Size Distribution, Flowrate Ratio ' + flowrates[indLeg]+", N = {}".format(len(i)),fontweight='bold', fontsize=14)
    plt.xlim([(min(value for sublist in radius for value in sublist))*2 -50, (max(val for sub in radius for val in sub))*2 +50])
    plt.legend()
    plt.ylabel('Count', fontsize=12)
    plt.xlabel('Droplet Diameter [\u03BCm]', fontsize=12)
    plt.savefig("{}.png".format(ind+len(radius)+indLeg), dpi=300)


    # Print fit values
    print("Fit Values: {:.2f} and {:.2f}".format(mu, std))









plt.figure(1)
plt.legend(framealpha=.95, prop={'size': 12})
plt.xlim([(min(value for sublist in radius for value in sublist))*2 -50, (max(val for sub in radius for val in sub))*2 +50])
aspect_ratio = 16 / 9
fig = plt.gcf()
fig.set_size_inches(fig.get_size_inches() * aspect_ratio)
plt.savefig(filename0, dpi=300)

plt.figure(2)
plt.legend(framealpha=.97, prop={'size': 12})
plt.xlim([(min(value for sublist in radius for value in sublist))*2 -50, (max(val for sub in radius for val in sub))*2 +50])
aspect_ratio = 16 / 9
fig = plt.gcf()
fig.set_size_inches(fig.get_size_inches() * aspect_ratio)
plt.savefig(filename1, dpi=300)


# # Fit a normal distribution to the data: mean and standard deviation
# mu, std = norm.fit(diameters)
#
# # Plot the PDF.
# # xmin, xmax = plt.xlim()
# # x = np.linspace(xmin, xmax, 100)
# p = norm.pdf(diameters, mu, std)
#
# plt.plot(diameters, p, 'k', linewidth=2)
# title = "Fit Values: {:.2f} and {:.2f}".format(mu, std)
# plt.title(title)

# plt.hist(diameters, alpha=0.5, bins=20)
# plt.title('Size distribution')
# plt.ylabel('Count')
# plt.xlabel('Droplet diameter [um]')
# plt.show()