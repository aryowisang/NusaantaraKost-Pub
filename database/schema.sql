-- Schema for Sistem Manajemen Kos Nusantara (NusantaraKos)
CREATE DATABASE IF NOT EXISTS `nusakost` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `nusakost`;

-- Table 1: Kamar
CREATE TABLE IF NOT EXISTS `kamar` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nomor` VARCHAR(20) NOT NULL UNIQUE,
    `tipe` VARCHAR(50) NOT NULL,
    `harga` INT NOT NULL,
    `status` VARCHAR(20) DEFAULT 'Tersedia',
    `fasilitas` TEXT,
    `deskripsi` TEXT,
    `gambar` VARCHAR(255) DEFAULT 'kamar-standard.png'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table 2: Penghuni
CREATE TABLE IF NOT EXISTS `penghuni` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nama` VARCHAR(100) NOT NULL,
    `no_hp` VARCHAR(20) NOT NULL,
    `email` VARCHAR(100),
    `alamat` TEXT,
    `pekerjaan` VARCHAR(50) DEFAULT 'Mahasiswa',
    `foto_ktp` VARCHAR(255),
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table 3: Sewa
CREATE TABLE IF NOT EXISTS `sewa` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `id_kamar` INT NOT NULL,
    `id_penghuni` INT NOT NULL,
    `tanggal_masuk` DATE NOT NULL,
    `tanggal_keluar` DATE NOT NULL,
    `lama_sewa` INT NOT NULL,
    `total_bayar` INT NOT NULL,
    `status_sewa` VARCHAR(20) DEFAULT 'Aktif',
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`id_kamar`) REFERENCES `kamar`(`id`) ON DELETE RESTRICT,
    FOREIGN KEY (`id_penghuni`) REFERENCES `penghuni`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Seed Data
INSERT INTO `kamar` (`nomor`, `tipe`, `harga`, `status`, `fasilitas`, `deskripsi`, `gambar`) VALUES
('101', 'Standard', 1100000, 'Tersedia', 'Wi-Fi 100M, Kasur Springbed, Lemari, Kipas Angin', 'Kamar bersih, tenang, dan memiliki pencahayaan alami yang baik.', 'kamar-standard.png'),
('102', 'Standard', 1150000, 'Tersedia', 'Wi-Fi 100M, Meja Belajar, Lemari, Kipas Angin', 'Kamar tipe standard posisi dekat ke area parkir dengan ventilasi udara segar.', 'kamar-standard.png'),
('201', 'Deluxe AC', 1650000, 'Tersedia', 'AC Cool, Kamar Mandi Dalam, Water Heater, Wi-Fi 100M', 'Kamar modern ber-AC dengan kamar mandi pribadi dan pemanas air shower.', 'kamar-deluxe.png'),
('202', 'Deluxe AC', 1700000, 'Terisi', 'AC Cool, Kamar Mandi Dalam, Kasur Queen, Wi-Fi 100M', 'Kamar Deluxe AC lantai 2 dengan jendela menghadap pemandangan taman.', 'kamar-deluxe.png'),
('301', 'VIP Suite', 2200000, 'Tersedia', 'Balkon Privat, AC 1 PK, Smart TV 32", Kulkas Mini', 'Tipe kamar eksklusif terluas dilengkapi balkon pribadi dan Smart TV.', 'kamar-vip.png'),
('302', 'VIP Suite', 2300000, 'Tersedia', 'Balkon Privat, AC 1 PK, Smart TV 43", Kulkas Mini', 'Kamar suite paling istimewa dengan view terbaik kota Yogyakarta.', 'kamar-vip.png');

INSERT INTO `penghuni` (`nama`, `no_hp`, `email`, `alamat`, `pekerjaan`) VALUES
('Budi Santoso', '081234567891', 'budi@mail.com', 'Jl. Malioboro No. 45, Yogyakarta', 'Mahasiswa UGM'),
('Siti Nurhaliza', '081298765432', 'siti@mail.com', 'Jl. Gejayan No. 12, Sleman', 'Mahasiswa UNY');

INSERT INTO `sewa` (`id_kamar`, `id_penghuni`, `tanggal_masuk`, `tanggal_keluar`, `lama_sewa`, `total_bayar`, `status_sewa`) VALUES
(4, 2, '2026-01-01', '2026-07-01', 6, 10200000, 'Aktif');
