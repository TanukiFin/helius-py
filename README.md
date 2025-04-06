
# Enhanced Transactions API
https://docs.helius.dev/solana-apis/enhanced-transactions-api

# Digital Asset Standard (DAS) API
https://docs.helius.dev/compression-and-das-api/digital-asset-standard-das-api

| 功能名稱                    | 說明                                                               | API 方法名稱               |
|---------------------------|--------------------------------------------------------------------|----------------------------|
| Get Asset                 | 根據資產 ID 取得單一資產資訊。                                    | `getAsset`                 |
| Get Asset Batch           | 根據多個資產 ID 一次取得多個資產資訊。                            | `getAssetBatch`           |
| Get Asset Proof           | 根據資產 ID 取得壓縮資產的 Merkle 證明。                          | `getAssetProof`           |
| Get Asset Proof Batch     | 根據多個資產 ID 一次取得多個 Merkle 證明。                        | `getAssetProofBatch`      |
| Search Assets             | 使用多種參數搜尋資產。                                            | `searchAssets`            |
| Get Assets by Owner       | 根據地址取得該地址擁有的資產清單。                                | `getAssetsByOwner`        |
| Get Assets by Authority   | 根據特定 authority 取得其相關資產清單。                           | `getAssetsByAuthority`    |
| Get Assets by Creator     | 根據創建者地址取得其創建的資產清單。                              | `getAssetsByCreator`      |
| Get Assets by Group       | 根據群組鍵與值取得資產清單。                                      | `getAssetsByGroup`        |
| Get Signatures For Asset  | 取得與壓縮資產相關的交易簽章紀錄。                                | `getSignaturesForAsset`   |
| Get Token Accounts        | 取得特定 mint 或 owner 所有的 token 帳戶資訊。                    | `getTokenAccounts`        |
| Get Nft Editions          | 取得特定主 NFT 的所有 edition NFTs 資訊。                        | `getNftEditions`          |


# HTTP
Solana 節點使用 JSON-RPC 2.0 規格接受 HTTP 請求。