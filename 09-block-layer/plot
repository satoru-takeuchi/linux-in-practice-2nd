#!/usr/bin/python3

import numpy as np
from PIL import Image
import matplotlib
import os

matplotlib.use('Agg')

import matplotlib.pyplot as plt

SCHEDULERS = ["mq-deadline", "none"]
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.sans-serif'] = "TakaoPGothic"

def do_plot(fig, pattern):
    # Ubuntu 20.04のmatplotlibのバグを回避するために一旦pngで保存してからjpgに変換している
    # https://bugs.launchpad.net/ubuntu/+source/matplotlib/+bug/1897283?comments=all
    pngfn = pattern + ".png"
    jpgfn = pattern + ".jpg"
    fig.savefig(pngfn)
    Image.open(pngfn).convert("RGB").save(jpgfn)
    os.remove(pngfn)

def plot_iops(type):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for sched in SCHEDULERS:
        x, y, _ = np.loadtxt("{}/randwrite-{}.txt".format(type, sched), unpack=True)
        ax.scatter(x,y,s=3)
    ax.set_title("I/Oスケジューラが有効な場合と無効な場合のIOPS")
    ax.set_xlabel("並列度")
    ax.set_ylabel("IOPS")
    ax.set_ylim(0)
    ax.legend(SCHEDULERS)
    do_plot(fig, type + "-iops")

def plot_iops_compare(type):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    x1, y1, _ = np.loadtxt("{}/randwrite-{}.txt".format(type, "mq-deadline"), unpack=True)
    _, y2, _ = np.loadtxt("{}/randwrite-{}.txt".format(type, "none"), unpack=True)
    y3 = (y1 / y2 - 1) * 100
    ax.scatter(x1,y3, s=3)
    ax.set_title("I/Oスケジューラの有効化によるIOPSの変化率[%]")
    ax.set_xlabel("並列度")
    ax.set_ylabel("IOPSの変化率[%]")
    ax.set_yticks([-20, 0, 20])

    do_plot(fig, type + "-iops-compare")

def plot_latency(type):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for sched in SCHEDULERS:
        x, _, y = np.loadtxt("{}/randwrite-{}.txt".format(type, sched), unpack=True)
        for i in range(len(y)):
            y[i] /= 1000000
        ax.scatter(x,y,s=3)
    ax.set_title("I/Oスケジューラが有効な場合と無効な場合のレイテンシ")
    ax.set_xlabel("並列度")
    ax.set_ylabel("レイテンシ[ミリ秒]")
    ax.set_ylim(0)
    ax.legend(SCHEDULERS)

    do_plot(fig, type + "-latency")

def plot_latency_compare(type):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    x1, _, y1 = np.loadtxt("{}/randwrite-{}.txt".format(type, "mq-deadline"), unpack=True)
    _, _, y2 = np.loadtxt("{}/randwrite-{}.txt".format(type, "none"), unpack=True)
    y3 = (y1 / y2 - 1) * 100
    ax.scatter(x1,y3, s=3)
    ax.set_title("I/Oスケジューラの有効化によるレイテンシの変化率[%]")
    ax.set_xlabel("並列度")
    ax.set_ylabel("レイテンシの変化率[%]")
    ax.set_yticks([-20,0,20])

    do_plot(fig, type + "-latency-compare")

for type in ["HDD", "SSD"]:
    plot_iops(type)
    plot_iops_compare(type)
    plot_latency_compare(type)
    plot_latency(type)
