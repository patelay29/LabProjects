#%%

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd


#read in minor from Results.csv
pdResults = pd.read_csv('ResultsTemplate.csv')
minor = pdResults['Minor']
minorRadius = minor/2
radius = [minorRadius]






flowrates = ["140:6, 7 wt% Template"]
t10p = ['#1f77b4']

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
    plt.title('Microgel Size, Normalized',fontweight='bold', fontsize=20)
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
    plt.title('Microgel Size',fontweight='bold', fontsize=20)
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
    plt.title('Microgel Size, Flow Ratio ' + flowrates[indLeg] + ", N = {}".format(len(i)),fontweight='bold', fontsize=14)
    plt.xlim([(min(value for sublist in radius for value in sublist))*2 -50, (max(val for sub in radius for val in sub))*2 +50])
    plt.legend(loc='upper right')
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
    plt.title('Microgel Size, Flow Ratio ' + flowrates[indLeg]+", N = {}".format(len(i)),fontweight='bold', fontsize=14)
    plt.xlim([(min(value for sublist in radius for value in sublist))*2 -50, (max(val for sub in radius for val in sub))*2 +50])
    plt.legend(loc='upper right')
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
# %%

# %%
