// Untuk hapus data yang bukan bulan Januari
db.collectionName.deleteMany({
    $expr: {
        $not: {
            $eq: [{ $month: { $toDate: "$time" } }, 1]
        }
    }
})