<?php
//Simpanlah dengan nama file : Pengembalian.php
require_once 'database.php';
class Pengembalian 
{
    private $db;
    private $table = 'pengembalian';
    public $kode_pengembalian = "";
    public $taggal_pengembalian = "";
    public $denda = "";
    public $kode_buku = "";
    public $kode_anggota = "";
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
    public function get_by_kode_pengembalian(int $kode_pengembalian)
    {
        $query = "SELECT * FROM $this->table WHERE kode_pengembalian = $kode_pengembalian";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_pengembalian`,`taggal_pengembalian`,`denda`,`kode_buku`,`kode_anggota`) VALUES ('$this->kode_pengembalian','$this->taggal_pengembalian','$this->denda','$this->kode_buku','$this->kode_anggota')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_pengembalian = '$this->kode_pengembalian', taggal_pengembalian = '$this->taggal_pengembalian', denda = '$this->denda', kode_buku = '$this->kode_buku', kode_anggota = '$this->kode_anggota' 
        WHERE id_pengembalian = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_pengembalian($kode_pengembalian): int
    {
        $query = "UPDATE $this->table SET kode_pengembalian = '$this->kode_pengembalian', taggal_pengembalian = '$this->taggal_pengembalian', denda = '$this->denda', kode_buku = '$this->kode_buku', kode_anggota = '$this->kode_anggota' 
        WHERE kode_pengembalian = $kode_pengembalian";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_pengembalian = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_pengembalian($kode_pengembalian): int
    {
        $query = "DELETE FROM $this->table WHERE kode_pengembalian = $kode_pengembalian";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>