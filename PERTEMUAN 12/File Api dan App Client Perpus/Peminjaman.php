<?php
//Simpanlah dengan nama file : Peminjaman.php
require_once 'database.php';
class Peminjaman 
{
    private $db;
    private $table = 'peminjaman';
    public $kode_peminjaman = "";
    public $tanggal_peminjaman = "";
    public $tanggal_kembali = "";
    public $kode_buku = "";
    public $kode_angota = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_kode_peminjaman(int $kode_peminjaman)
    {
        $query = "SELECT * FROM $this->table WHERE kode_peminjaman = $kode_peminjaman";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_peminjaman`,`tanggal_peminjaman`,`tanggal_kembali`,`kode_buku`,`kode_angota`) VALUES ('$this->kode_peminjaman','$this->tanggal_peminjaman','$this->tanggal_kembali','$this->kode_buku','$this->kode_angota')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_peminjaman = '$this->kode_peminjaman', tanggal_peminjaman = '$this->tanggal_peminjaman', tanggal_kembali = '$this->tanggal_kembali', kode_buku = '$this->kode_buku', kode_angota = '$this->kode_angota' 
        WHERE id_peminjaman = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_peminjaman($kode_peminjaman): int
    {
        $query = "UPDATE $this->table SET kode_peminjaman = '$this->kode_peminjaman', tanggal_peminjaman = '$this->tanggal_peminjaman', tanggal_kembali = '$this->tanggal_kembali', kode_buku = '$this->kode_buku', kode_angota = '$this->kode_angota' 
        WHERE kode_peminjaman = $kode_peminjaman";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_peminjaman = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_peminjaman($kode_peminjaman): int
    {
        $query = "DELETE FROM $this->table WHERE kode_peminjaman = $kode_peminjaman";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>