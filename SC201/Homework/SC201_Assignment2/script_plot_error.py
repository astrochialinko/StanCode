#!/usr/local/anaconda3/envs/stanCode37/bin/python3
"""
File: script_plot_error.py
Name: Chia-Lin Ko
Create Date: May 16, 2021
------------------------
This program aims to plot the error
"""
import numpy as np
import matplotlib.pyplot as plt

PATH = './Milestone1/'
TXT_LST = ['error_word.txt', 'error_char.txt']
TXT_LABLE = ['word', 'character']
MARKER_LST = ['o', 's']
COLOE_LST = ['C0', 'C7']

def main():

    plot_diff_epoch()
    plot_diff_feature()

def plot_diff_epoch():
    numEpochs_lst = [40, 50, 60, 70, 80, 90]
    train_error_lst = [0.0360, 0.0248, 0.0189, 0.0146, 0.0124, 0.0096]
    validation_error_lst = [0.2673, 0.2659, 0.2606, 0.2614, 0.2631, 0.2659]

    fig, axs = plt.subplots(1, 3, figsize=(18, 4))
    axs[0].plot(numEpochs_lst, train_error_lst, 'o-', markeredgecolor='k', label= 'Training Error')
    axs[0].set_xlabel('Epochs')
    axs[0].set_ylabel('Error')
    axs[0].legend()
    axs[1].plot(numEpochs_lst, validation_error_lst, 's-', c='C1', markeredgecolor='k', label='Validation Error')
    axs[1].set_xlabel('Epochs')
    axs[1].legend()
    axs[2].plot(numEpochs_lst, train_error_lst, 'o-', markeredgecolor='k', label= 'Training Error')
    axs[2].plot(numEpochs_lst, validation_error_lst, 's-', markeredgecolor='k', label='Validation Error')
    axs[2].set_xlabel('Epochs')
    plt.legend()
    plt.savefig('%serror_diff_epoch.pdf'%(PATH))
    plt.show()

def plot_diff_feature():
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))
    plt.rcParams["font.family"] = "serif"
    
    for i, txt in enumerate(TXT_LST):
        error_arr = np.loadtxt('%s%s'%(PATH, TXT_LST[i]))
        epoch = error_arr.T[0]
        train_error = error_arr.T[1]
        validation_error = error_arr.T[2]
        axs[0].plot(epoch, validation_error, 's-', color=COLOE_LST[i], alpha=0.7, label= 'Validation Error (%s)'%(TXT_LABLE[i]), markeredgecolor='k')
        axs[1].plot(epoch, validation_error, 's-', color=COLOE_LST[i], alpha=0.7, label= 'Validation Error (%s)'%(TXT_LABLE[i]), markeredgecolor='k')
        axs[1].plot(epoch, train_error, 'o-', color=COLOE_LST[i], alpha=0.7, label= 'Training Error (%s)'%(TXT_LABLE[i]), markeredgecolor='k')        

    axs[0].set_xlabel('Epochs')
    axs[1].set_xlabel('Epochs')
    axs[0].set_ylabel('Error')
    axs[0].legend()
    axs[1].legend()
    plt.savefig('%serror_diff_feature.pdf'%(PATH))
    plt.show()

if __name__ == '__main__':
    main()